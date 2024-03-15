#!/usr/bin/env python3
import re
import ipdb

class MyString:
  def __init__(self, value=''):
    self.value = value
  @property
  def value(self):
    return self._value
  @value.setter
  def value(self, value):
    if type(value) is str:
      self._value = value
    else:
      print("The value must be a string.")
  def am_i_checker(self, mark):
    if self._value[-1] == mark:
      return True
    else:
      return False
  def is_sentence(self):
    return self.am_i_checker(".")
  def is_question(self):
    return self.am_i_checker("?")
  def is_exclamation(self):
    return self.am_i_checker("!")
  def count_sentences(self):
    sentences = re.split(r"[.?!]+", self._value)
    for sentence in sentences:
      if sentence == '':
        sentences.remove(sentence)
      else:
        pass
    print(sentences)
    return len(sentences)