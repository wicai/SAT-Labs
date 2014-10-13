#!/usr/bin/env python
from mchlrn.models import SATQuestion as sq

sq.objects.create(name = 'lots of numbers', question = '1 2 3 4 5 6 7 8 9 10 111111111 wow sure are lots of numbers huh', answer_A = '48', answer_B = '2', answer_C = '0', answer_D = '8', answer_E = '843', correct_answer = 'A', explanation = 'your guess is as good as mine', instructions = 'gg no re', channel = 'fake', channel_url = '', css = '')

sq.objects.create(name = 'lots of numbers 2 ', question = '1 2 only a few', answer_A = '48', answer_B = '2', answer_C = '0', answer_D = '8', answer_E = '843', correct_answer = 'A', explanation = 'your guess is as good as mine', instructions = 'gg no re', channel = 'fake', channel_url = '', css = '')

sq.objects.create(name = 'lots of numbers 3', question = '1 2 3 4 5 6 111111111 wow sure are lots of numbers huh', answer_A = '48', answer_B = '2', answer_C = '0', answer_D = '8', answer_E = '843', correct_answer = 'A', explanation = 'your guess is as good as mine', instructions = 'gg no re', channel = 'fake', channel_url = '', css = '')

sq.objects.create(name = 'lots of numbers 4', question = '4 3 2 43 2 1 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9  8 8 8 8 8 8 1 1 1 1  111111111 wow sure are lots of numbers huh', answer_A = '48', answer_B = '2', answer_C = '0', answer_D = '8', answer_E = '843', correct_answer = 'A', explanation = 'your guess is as good as mine', instructions = 'gg no re', channel = 'fake', channel_url = '', css = '')

sq.objects.create(name = 'lots of numbers 5', question = '8 2 10/5 2 58 88 8 8 8 8 1 90 48888 49392 1', answer_A = '48', answer_B = '2', answer_C = '0', answer_D = '8', answer_E = '843', correct_answer = 'A', explanation = 'your guess is as good as mine', instructions = 'gg no re', channel = 'fake', channel_url = '', css = '')

sq.objects.create(name = 'no numbers', question = 'why am i up late at night', answer_A = 'because i procrastinate', answer_B = 'because im tryna get shit done', answer_C = 'so tired', answer_D = 'what', answer_E = 'all of the above', correct_answer = 'E', explanation = 'idk', instructions = 'BANGIN ON TABLETOPS NO SUBSTITUTE', channel = 'fake', channel_url = '', css = '')

sq.objects.create(name = 'no numbers (actually theres just one)', question = 'wifey girlfriend and mistress 1', answer_A = 'backstreet freestyle', answer_B = 'because im tryna get shit done', answer_C = 'so tired', answer_D = 'what', answer_E = 'all above', correct_answer = 'A', explanation = 'kendrick lamar', instructions = 'fuck the industry', channel = 'fake', channel_url = '', css = '')
