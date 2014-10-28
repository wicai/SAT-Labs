# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'UserData.user'
        db.alter_column(u'mchlrn_userdata', 'user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True))

        # Changing field 'Answered_Sat_Q.user'
        db.alter_column(u'mchlrn_answered_sat_q', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.UserData']))

        # Changing field 'Answered_Math_Q.user'
        db.alter_column(u'mchlrn_answered_math_q', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.UserData']))

    def backwards(self, orm):

        # Changing field 'UserData.user'
        db.alter_column(u'mchlrn_userdata', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True))

        # Changing field 'Answered_Sat_Q.user'
        db.alter_column(u'mchlrn_answered_sat_q', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Changing field 'Answered_Math_Q.user'
        db.alter_column(u'mchlrn_answered_math_q', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'mchlrn.answered_math_q': {
            'Meta': {'object_name': 'Answered_Math_Q'},
            'correct': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'unanswered_q': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['mchlrn.Math_Q']", 'unique': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mchlrn.UserData']"})
        },
        u'mchlrn.answered_sat_q': {
            'Meta': {'object_name': 'Answered_Sat_Q'},
            'correct': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'unanswered_q': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mchlrn.SATQuestion']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mchlrn.UserData']"})
        },
        u'mchlrn.math_a': {
            'Meta': {'object_name': 'Math_A'},
            'answer': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'q': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mchlrn.Math_Q']"})
        },
        u'mchlrn.math_diagram': {
            'Meta': {'object_name': 'Math_Diagram'},
            'diagram': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mchlrn.Math_Q']"})
        },
        u'mchlrn.math_pred': {
            'Meta': {'object_name': 'Math_Pred'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'mchlrn.math_pred_item': {
            'Meta': {'object_name': 'Math_Pred_Item'},
            'col': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'row': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mchlrn.Math_Pred_Row']"}),
            'val': ('django.db.models.fields.FloatField', [], {})
        },
        u'mchlrn.math_pred_row': {
            'Meta': {'object_name': 'Math_Pred_Row'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'matrix': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mchlrn.Math_Pred']"}),
            'row': ('django.db.models.fields.IntegerField', [], {})
        },
        u'mchlrn.math_q': {
            'Meta': {'object_name': 'Math_Q'},
            'a': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'b': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'c': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'd': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'diagram_exists': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '600'}),
            'student_produced': ('django.db.models.fields.BooleanField', [], {})
        },
        u'mchlrn.math_q_processed': {
            'Meta': {'object_name': 'Math_Q_Processed'},
            'col_num': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.IntegerField', [], {}),
            'num_numbers': ('django.db.models.fields.IntegerField', [], {}),
            'orig_q': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['mchlrn.Math_Q']", 'unique': 'True'})
        },
        u'mchlrn.math_sp_a': {
            'Meta': {'object_name': 'Math_SP_A'},
            'answer': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'q': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mchlrn.Math_Q']"})
        },
        u'mchlrn.math_theta': {
            'Meta': {'object_name': 'Math_Theta'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'mchlrn.math_theta_item': {
            'Meta': {'object_name': 'Math_Theta_Item'},
            'col': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'row': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mchlrn.Math_Theta_Row']"}),
            'val': ('django.db.models.fields.FloatField', [], {})
        },
        u'mchlrn.math_theta_row': {
            'Meta': {'object_name': 'Math_Theta_Row'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'matrix': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mchlrn.Math_Theta']"}),
            'row': ('django.db.models.fields.IntegerField', [], {})
        },
        u'mchlrn.reading_a': {
            'Meta': {'object_name': 'Reading_A'},
            'answer': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'q': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mchlrn.Reading_Q']"})
        },
        u'mchlrn.reading_passage': {
            'Meta': {'object_name': 'Reading_Passage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'passage': ('django.db.models.fields.CharField', [], {'max_length': '10000'})
        },
        u'mchlrn.reading_passage_a': {
            'Meta': {'object_name': 'Reading_Passage_A'},
            'answer': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'q': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mchlrn.Reading_Passage_Q']"})
        },
        u'mchlrn.reading_passage_q': {
            'Meta': {'object_name': 'Reading_Passage_Q'},
            'a': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'b': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'c': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'd': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'passage': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mchlrn.Reading_Passage']"}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '600'})
        },
        u'mchlrn.reading_q': {
            'Meta': {'object_name': 'Reading_Q'},
            'a': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'b': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'c': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'd': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '600'})
        },
        u'mchlrn.sat_pred': {
            'Meta': {'object_name': 'Sat_Pred'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'mchlrn.sat_pred_item': {
            'Meta': {'object_name': 'Sat_Pred_Item'},
            'col': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'row': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mchlrn.Sat_Pred_Row']"}),
            'val': ('django.db.models.fields.FloatField', [], {})
        },
        u'mchlrn.sat_pred_row': {
            'Meta': {'object_name': 'Sat_Pred_Row'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'matrix': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mchlrn.Sat_Pred']"}),
            'row': ('django.db.models.fields.IntegerField', [], {})
        },
        u'mchlrn.sat_q_processed': {
            'Meta': {'object_name': 'Sat_Q_Processed'},
            'avg_score': ('django.db.models.fields.FloatField', [], {}),
            'col_num': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.IntegerField', [], {}),
            'num_numbers': ('django.db.models.fields.IntegerField', [], {}),
            'orig_q': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['mchlrn.SATQuestion']", 'unique': 'True'})
        },
        u'mchlrn.sat_theta': {
            'Meta': {'object_name': 'Sat_Theta'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'mchlrn.sat_theta_item': {
            'Meta': {'object_name': 'Sat_Theta_Item'},
            'col': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'row': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mchlrn.Sat_Theta_Row']"}),
            'val': ('django.db.models.fields.FloatField', [], {})
        },
        u'mchlrn.sat_theta_row': {
            'Meta': {'object_name': 'Sat_Theta_Row'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'matrix': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mchlrn.Sat_Theta']"}),
            'row': ('django.db.models.fields.IntegerField', [], {})
        },
        u'mchlrn.satquestion': {
            'Meta': {'object_name': 'SATQuestion'},
            'answer_A': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'answer_B': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'answer_C': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'answer_D': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'answer_E': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'channel': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'channel_url': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'correct_answer': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'css': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'difficulty': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'explanation': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructions': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'sub_category': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'})
        },
        u'mchlrn.userdata': {
            'Meta': {'object_name': 'UserData'},
            'col_num': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'mchlrn.writing_effective_a': {
            'Meta': {'object_name': 'Writing_Effective_A'},
            'answer': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'q': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mchlrn.Writing_Effective_Q']"})
        },
        u'mchlrn.writing_effective_q': {
            'Meta': {'object_name': 'Writing_Effective_Q'},
            'a': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'b': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'c': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'd': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '600'}),
            'underline_end': ('django.db.models.fields.IntegerField', [], {}),
            'underline_start': ('django.db.models.fields.IntegerField', [], {})
        },
        u'mchlrn.writing_grammar_a': {
            'Meta': {'object_name': 'Writing_Grammar_A'},
            'answer': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'q': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mchlrn.Writing_Grammar_Q']"})
        },
        u'mchlrn.writing_grammar_q': {
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '600'})
        },
        u'mchlrn.writing_passage': {
            'Meta': {'object_name': 'Writing_Passage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'passage': ('django.db.models.fields.CharField', [], {'max_length': '10000'})
        },
        u'mchlrn.writing_passage_a': {
            'Meta': {'object_name': 'Writing_Passage_A'},
            'answer': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'q': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mchlrn.Writing_Passage_Q']"})
        },
        u'mchlrn.writing_passage_q': {
            'Meta': {'object_name': 'Writing_Passage_Q'},
            'a': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'b': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'c': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'd': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'passage': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mchlrn.Writing_Passage']"}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '600'})
        }
    }

    complete_apps = ['mchlrn']