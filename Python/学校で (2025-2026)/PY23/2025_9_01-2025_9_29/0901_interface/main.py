# 0901_interface
# インスタンス
# 抽象基底クラスにて、全てが
# abstractメソッドのクラス
from abc import ABC, abstractmethod

class Player(ABC):
  @abstractmethod
  def play(self):
    pass

  @abstractmethod
  def stop(self):
    pass

# Points
# インタフェースは、口(くち)の定義だけで
# 実処理はー切ない

class MyPlayer(Player):
  def play(self):
    print('play')

  def stop(self):
    print('stop')

my = MyPlayer()
my.play()
my.stop()