class Pokemon:
  def __init__(self, name, level):
      self.name = name
      self.isKO = false
      self.level = level
      self.max_health = 10 * level
      self.health = self.max_health

  def lose_health(self,attack):
     self.health -= attack
     self.knock_out()
     if self.isKO:
         print(f'{self.name} has been knocked out')
     else:    
         print(f'{self.name} has {self.health} hit points left')


  def knock_out(self):
      if self.health <= 0:
          self.health *= 0
          self.isKO = true
          print(f'{self.name} has {self.health} hit points')

  def heal(self,heal_points):
      self.health += heal_points
      if self.health > self.max_health:
          self.health = self.max_health
          print(f'{self.name} has {self.health} hit points')


  def revive(self,heal_points):
      if self.isKO:
          self.heal(heal_points)
          print(f'{self.name} has been revived with {self.health} points')     
      else:
          print(f'{self.name} has {self.health}')                             
