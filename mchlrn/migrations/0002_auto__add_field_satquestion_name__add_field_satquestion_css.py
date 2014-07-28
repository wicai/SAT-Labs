# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SATQuestion.name'
        db.add_column('mchlrn_satquestion', 'name',
                      self.gf('django.db.models.fields.CharField')(default='ARG', max_length=128),
                      keep_default=False)

        # Adding field 'SATQuestion.css'
        db.add_column('mchlrn_satquestion', 'css',
                      self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SATQuestion.name'
        db.delete_column('mchlrn_satquestion', 'name')

        # Deleting field 'SATQuestion.css'
        db.delete_column('mchlrn_satquestion', 'css')


    models = {
        'mchlrn.answered_math_q': {
            'Meta': {'object_name': 'Answered_Math_Q'},
            'correct': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'unanswered_q': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mchlrn.Math_Q']", 'unique': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mchlrn.User']"})
        },
        'mchlrn.math_a': {
            'Meta': {'object_name': 'Math_A'},
            'answer': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'q': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mchlrn.Math_Q']"})
        },
        'mchlrn.math_diagram': {
            'Meta': {'object_name': 'Math_Diagram'},
            'diagram': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mchlrn.Math_Q']"})
        },
        'mchlrn.math_pred': {
            'Meta': {'object_name': 'Math_Pred'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'mchlrn.math_pred_item': {
            'Meta': {'object_name': 'Math_Pred_Item'},
            'col': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'row': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mchlrn.Math_Pred_Row']"}),
            'val': ('django.db.models.fields.FloatField', [], {})
        },
        'mchlrn.math_pred_row': {
            'Meta': {'object_name': 'Math_Pred_Row'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'matrix': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mchlrn.Math_Pred']"}),
            'row': ('django.db.models.fields.IntegerField', [], {})
        },
        'mchlrn.math_q': {
            'Meta': {'object_name': 'Math_Q'},
            'a': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'b': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'c': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'd': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'diagram_exists': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '600'}),
            'student_produced': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'mchlrn.math_q_processed': {
            'Meta': {'object_name': 'Math_Q_Processed'},
            'col_num': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.IntegerField', [], {}),
            'num_numbers': ('django.db.models.fields.IntegerField', [], {}),
            'orig_q': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mchlrn.Math_Q']", 'unique': 'True'})
        },
        'mchlrn.math_sp_a': {
            'Meta': {'object_name': 'Math_SP_A'},
            'answer': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'q': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mchlrn.Math_Q']"})
        },
        'mchlrn.math_theta': {
            'Meta': {'object_name': 'Math_Theta'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'mchlrn.math_theta_item': {
            'Meta': {'object_name': 'Math_Theta_Item'},
            'col': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'row': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mchlrn.Math_Theta_Row']"}),
            'val': ('django.db.models.fields.FloatField', [], {})
        },
        'mchlrn.math_theta_row': {
            'Meta': {'object_name': 'Math_Theta_Row'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'matrix': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mchlrn.Math_Theta']"}),
            'row': ('django.db.models.fields.IntegerField', [], {})
        },
        'mchlrn.reading_a': {
            'Meta': {'object_name': 'Reading_A'},
            'answer': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'q': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mchlrn.Reading_Q']"})
        },
        'mchlrn.reading_passage': {
            'Meta': {'object_name': 'Reading_Passage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'passage': ('django.db.models.fields.CharField', [], {'max_length': '10000'})
        },
        'mchlrn.reading_passage_a': {
            'Meta': {'object_name': 'Reading_Passage_A'},
            'answer': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'q': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mchlrn.Reading_Passage_Q']"})
        },
        'mchlrn.reading_passage_q': {
            'Meta': {'object_name': 'Reading_Passage_Q'},
            'a': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'b': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'c': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'd': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'passage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mchlrn.Reading_Passage']"}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '600'})
        },
        'mchlrn.reading_q': {
            'Meta': {'object_name': 'Reading_Q'},
            'a': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'b': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'c': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'd': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '600'})
        },
        'mchlrn.satquestion': {
            'Meta': {'object_name': 'SATQuestion'},
            'answer_A': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'answer_B': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'answer_C': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'answer_D': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'answer_E': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'channel': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'channel_url': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'correct_answer': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'css': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'difficulty': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'explanation': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructions': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        'mchlrn.user': {
            'Meta': {'object_name': 'User'},
            'col_num': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'mchlrn.writing_effective_a': {
            'Meta': {'object_name': 'Writing_Effective_A'},
            'answer': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'q': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mchlrn.Writing_Effective_Q']"})
        },
        'mchlrn.writing_effective_q': {
            'Meta': {'object_name': 'Writing_Effective_Q'},
            'a': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'b': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'c': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'd': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '600'}),
            'underline_end': ('django.db.models.fields.IntegerField', [], {}),
            'underline_start': ('django.db.models.fields.IntegerField', [], {})
        },
        'mchlrn.writing_grammar_a': {
            'Meta': {'object_name': 'Writing_Grammar_A'},
            'answer': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'q': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mchlrn.Writing_Grammar_Q']"})
        },
        'mchlrn.writing_grammar_q': {
            'Meta': {'object_name': 'Writing_Grammar_Q'},
            'a_underline_end': ('django.db.models.fields.IntegerField', [], {}),
            'a_underline_start': ('django.db.models.fields.IntegerField', [], {}),
            'b_underline_end': ('django.db.models.fields.IntegerField', [], {}),
            'b_underline_start': ('django.db.models.fields.IntegerField', [], {}),
            'c_underline_end': ('django.db.models.fields.IntegerField', [], {}),
            'c_underline_start': ('django.db.models.fields.IntegerField', [], {}),
            'd_underline_end': ('django.db.models.fields.IntegerField', [], {}),
            'd_underline_start': ('django.db.models.fields.IntegerField', [], {}),
            'e_underline_end': ('django.db.models.fields.IntegerField', [], {}),
            'e_underline_start': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '600'})
        },
        'mchlrn.writing_passage': {
            'Meta': {'object_name': 'Writing_Passage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'passage': ('django.db.models.fields.CharField', [], {'max_length': '10000'})
        },
        'mchlrn.writing_passage_a': {
            'Meta': {'object_name': 'Writing_Passage_A'},
            'answer': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'q': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mchlrn.Writing_Passage_Q']"})
        },
        'mchlrn.writing_passage_q': {
            'Meta': {'object_name': 'Writing_Passage_Q'},
            'a': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'b': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'c': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'd': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'passage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mchlrn.Writing_Passage']"}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '600'})
        }
    }

    complete_apps = ['mchlrn']