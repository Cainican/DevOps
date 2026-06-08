class Player {
    constructor() {
        this.pos = createVector(-800, -playerSize, 0);
        this.size = playerSize;
        this.velocity = createVector(0, 0, 0);
        this.grounded = false;
        this.speed = 1;
        this.jumpSpeed = 10;
        this.facingAngle = 0;
    }

    update() {
        this.handleMovement();
        this.handleGroundAndJump();
        this.applyGravity();

        // 水平方向は個別に解決
        this.resolveHorizontalCollision();
        // 垂直方向も個別に解決
        this.resolveVerticalCollision();

        // 摩擦処理などは各軸の速度に対して行う
        this.velocity.mult(0.9);
    }

    // カメラの向きに応じた前後左右移動
    handleMovement() {
    // 前方向（カメラの向き）
    let forward = createVector(
        sin(radians(camAngle)),
        0,
        cos(radians(camAngle))
    );
    // 右方向（前方向を90度回転させたベクトル）
    let right = createVector(
        cos(radians(camAngle)),
        0,
        -sin(radians(camAngle))
    );

    let moveDir = createVector(0, 0, 0);

    // TODO: Wキーで前進
    if (keyIsDown(87)) { // W
        this.velocity.add(p5.Vector.mult(forward, this.speed));
    }
    // TODO: Sキーで後退
    if (keyIsDown(83)) { // S
        this.velocity.add(p5.Vector.mult(forward, -this.speed));
    }
    // TODO: Aキーで左に移動
    if (keyIsDown(65)) { // A
        this.velocity.add(p5.Vector.mult(right, this.speed));
    }
    // TODO: Dキーで右に移動
    if (keyIsDown(68)) { // D
        this.velocity.add(p5.Vector.mult(right, -this.speed));
    }
}

    handleGroundAndJump() {
        const jumpSpeed = this.jumpSpeed;
        const groundThreshold = -1;
        if (this.pos.y >= groundThreshold) {
            this.pos.y = 0;
            this.velocity.y = 0;
            this.grounded = true;
            // TODO: Spaceでジャンプ
            if (keyIsDown(32)) {
                this.velocity.y = -jumpSpeed;
                this.grounded = false;
            }
        } else {
            this.grounded = false;
            // Xで強制下降
            if (keyIsDown(88)) {
                this.velocity.y = jumpSpeed;
            }
        }
    }

    applyGravity() {
        const gravity = 0.5;
        this.velocity.y += gravity;
    }

    // 垂直方向の移動と衝突処理（Y軸のみ）
    resolveVerticalCollision() {
        let newY = this.pos.y + this.velocity.y;
        let verticalTestPos = createVector(this.pos.x, newY, this.pos.z);
        let verticalCollision = false;
        let collidedObstacle = null;

        for (let obs of obstacles) {
            if (sphereBoxCollision(verticalTestPos, this.size / 2, obs)) {
                verticalCollision = true;
                collidedObstacle = obs;
                break;
            }
        }

        if (!verticalCollision) {
            // 衝突がなければそのまま移動
            this.pos.y = newY;
        } else {
            // 衝突があった場合、上昇中か落下中かで処理を分ける
            if (this.velocity.y > 0) {
                // 落下中の場合：障害物の上に着地させる
                if (collidedObstacle) {
                    // 障害物の上面の Y 座標
                    let topY = -(collidedObstacle.pos.y + collidedObstacle.h / 2 - 1);
                    // プレイヤーの底部が障害物の上面に触れるように調整
                    this.pos.y = topY - this.size / 2;
                }
                this.grounded = true;
            } else if (this.velocity.y < 0) {
                // 上昇中の場合：障害物の下側にぶつかったとみなす
                if (collidedObstacle) {
                    // 障害物の底面の Y 座標を計算
                    // 障害物は translate(this.pos.x, -(box.pos.y + box.h/2 - 1), this.pos.z) で描画されるので、
                    // 障害物の底面は、障害物の中心 - (h/2) となる。ここでは底面（障害物の下側）の Y 座標:
                    let bottomY = -(collidedObstacle.pos.y - collidedObstacle.h / 2 - 1);
                    // プレイヤーの頭部が障害物の底面に触れるように調整
                    this.pos.y = bottomY + this.size / 2;
                }
                // 上昇中の場合は着地状態にはしない
                this.grounded = false;
            }
            // 衝突時は垂直方向の速度をリセット
            this.velocity.y = 0;
        }
    }

    // 水平方向の移動と衝突処理（X, Z軸）
    resolveHorizontalCollision() {
        // X軸個別処理
        let newX = this.pos.x + this.velocity.x;
        let testPosX = createVector(newX, this.pos.y, this.pos.z);
        let collisionX = false;
        for (let obs of obstacles) {
            if (sphereBoxCollision(testPosX, this.size / 2, obs)) {
                collisionX = true;
                break;
            }
        }
        if (!collisionX) {
            this.pos.x = newX;
        } else {
            this.velocity.x = 0;
        }

        // Z軸個別処理
        let newZ = this.pos.z + this.velocity.z;
        let testPosZ = createVector(this.pos.x, this.pos.y, newZ);
        let collisionZ = false;
        for (let obs of obstacles) {
            if (sphereBoxCollision(testPosZ, this.size / 2, obs)) {
                collisionZ = true;
                break;
            }
        }
        if (!collisionZ) {
            this.pos.z = newZ;
        } else {
            this.velocity.z = 0;
        }
    }

    display() {
        push();
        translate(this.pos.x, this.pos.y, this.pos.z);

        if (this.facingAngle !== undefined) {
            rotateY(radians(this.facingAngle));
        }

        fill(100, 100, 200);
        noStroke();
        sphere(this.size / 2);
        pop();
    }
}