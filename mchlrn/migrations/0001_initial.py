# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SATQuestion'
        db.create_table('mchlrn_satquestion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('answer_A', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('answer_B', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('answer_C', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('answer_D', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('answer_E', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('correct_answer', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('explanation', self.gf('django.db.models.fields.CharField')(max_length=2048, null=True, blank=True)),
            ('instructions', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('channel', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('channel_url', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('difficulty', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('mchlrn', ['SATQuestion'])

        # Adding model 'User'
        db.create_table('mchlrn_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('col_num', self.gf('django.db.models.fields.IntegerField')()),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('mchlrn', ['User'])

        # Adding model 'Answered_Math_Q'
        db.create_table('mchlrn_answered_math_q', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('unanswered_q', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mchlrn.Math_Q'], unique=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.User'])),
            ('correct', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('mchlrn', ['Answered_Math_Q'])

        # Adding model 'Math_Pred'
        db.create_table('mchlrn_math_pred', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('mchlrn', ['Math_Pred'])

        # Adding model 'Math_Pred_Row'
        db.create_table('mchlrn_math_pred_row', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('row', self.gf('django.db.models.fields.IntegerField')()),
            ('matrix', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.Math_Pred'])),
        ))
        db.send_create_signal('mchlrn', ['Math_Pred_Row'])

        # Adding model 'Math_Pred_Item'
        db.create_table('mchlrn_math_pred_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('row', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.Math_Pred_Row'])),
            ('col', self.gf('django.db.models.fields.IntegerField')()),
            ('val', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('mchlrn', ['Math_Pred_Item'])

        # Adding model 'Math_Theta'
        db.create_table('mchlrn_math_theta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('mchlrn', ['Math_Theta'])

        # Adding model 'Math_Theta_Row'
        db.create_table('mchlrn_math_theta_row', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('row', self.gf('django.db.models.fields.IntegerField')()),
            ('matrix', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.Math_Theta'])),
        ))
        db.send_create_signal('mchlrn', ['Math_Theta_Row'])

        # Adding model 'Math_Theta_Item'
        db.create_table('mchlrn_math_theta_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('row', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.Math_Theta_Row'])),
            ('col', self.gf('django.db.models.fields.IntegerField')()),
            ('val', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('mchlrn', ['Math_Theta_Item'])

        # Adding model 'Math_Q_Processed'
        db.create_table('mchlrn_math_q_processed', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('orig_q', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mchlrn.Math_Q'], unique=True)),
            ('col_num', self.gf('django.db.models.fields.IntegerField')()),
            ('length', self.gf('django.db.models.fields.IntegerField')()),
            ('num_numbers', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('mchlrn', ['Math_Q_Processed'])

        # Adding model 'Math_Q'
        db.create_table('mchlrn_math_q', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=600)),
            ('diagram_exists', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('student_produced', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('a', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('b', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('c', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('d', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('mchlrn', ['Math_Q'])

        # Adding model 'Math_Diagram'
        db.create_table('mchlrn_math_diagram', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.Math_Q'])),
            ('diagram', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('mchlrn', ['Math_Diagram'])

        # Adding model 'Math_A'
        db.create_table('mchlrn_math_a', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('q', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.Math_Q'])),
            ('answer', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('mchlrn', ['Math_A'])

        # Adding model 'Math_SP_A'
        db.create_table('mchlrn_math_sp_a', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('q', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.Math_Q'])),
            ('answer', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('mchlrn', ['Math_SP_A'])

        # Adding model 'Reading_Passage'
        db.create_table('mchlrn_reading_passage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('passage', self.gf('django.db.models.fields.CharField')(max_length=10000)),
        ))
        db.send_create_signal('mchlrn', ['Reading_Passage'])

        # Adding model 'Reading_Passage_Q'
        db.create_table('mchlrn_reading_passage_q', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=600)),
            ('a', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('b', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('c', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('d', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('passage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.Reading_Passage'])),
        ))
        db.send_create_signal('mchlrn', ['Reading_Passage_Q'])

        # Adding model 'Reading_Passage_A'
        db.create_table('mchlrn_reading_passage_a', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('q', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.Reading_Passage_Q'])),
            ('answer', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('mchlrn', ['Reading_Passage_A'])

        # Adding model 'Reading_Q'
        db.create_table('mchlrn_reading_q', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=600)),
            ('a', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('b', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('c', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('d', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('mchlrn', ['Reading_Q'])

        # Adding model 'Reading_A'
        db.create_table('mchlrn_reading_a', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('q', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.Reading_Q'])),
            ('answer', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('mchlrn', ['Reading_A'])

        # Adding model 'Writing_Passage'
        db.create_table('mchlrn_writing_passage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('passage', self.gf('django.db.models.fields.CharField')(max_length=10000)),
        ))
        db.send_create_signal('mchlrn', ['Writing_Passage'])

        # Adding model 'Writing_Passage_Q'
        db.create_table('mchlrn_writing_passage_q', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=600)),
            ('a', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('b', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('c', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('d', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('passage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.Writing_Passage'])),
        ))
        db.send_create_signal('mchlrn', ['Writing_Passage_Q'])

        # Adding model 'Writing_Passage_A'
        db.create_table('mchlrn_writing_passage_a', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('q', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.Writing_Passage_Q'])),
            ('answer', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('mchlrn', ['Writing_Passage_A'])

        # Adding model 'Writing_Effective_Q'
        db.create_table('mchlrn_writing_effective_q', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=600)),
            ('underline_start', self.gf('django.db.models.fields.IntegerField')()),
            ('underline_end', self.gf('django.db.models.fields.IntegerField')()),
            ('a', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('b', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('c', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('d', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('mchlrn', ['Writing_Effective_Q'])

        # Adding model 'Writing_Effective_A'
        db.create_table('mchlrn_writing_effective_a', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('q', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.Writing_Effective_Q'])),
            ('answer', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('mchlrn', ['Writing_Effective_A'])

        # Adding model 'Writing_Grammar_Q'
        db.create_table('mchlrn_writing_grammar_q', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=600)),
            ('a_underline_start', self.gf('django.db.models.fields.IntegerField')()),
            ('a_underline_end', self.gf('django.db.models.fields.IntegerField')()),
            ('b_underline_start', self.gf('django.db.models.fields.IntegerField')()),
            ('b_underline_end', self.gf('django.db.models.fields.IntegerField')()),
            ('c_underline_start', self.gf('django.db.models.fields.IntegerField')()),
            ('c_underline_end', self.gf('django.db.models.fields.IntegerField')()),
            ('d_underline_start', self.gf('django.db.models.fields.IntegerField')()),
            ('d_underline_end', self.gf('django.db.models.fields.IntegerField')()),
            ('e_underline_start', self.gf('django.db.models.fields.IntegerField')()),
            ('e_underline_end', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('mchlrn', ['Writing_Grammar_Q'])

        # Adding model 'Writing_Grammar_A'
        db.create_table('mchlrn_writing_grammar_a', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('q', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.Writing_Grammar_Q'])),
            ('answer', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('mchlrn', ['Writing_Grammar_A'])


    def backwards(self, orm):
        # Deleting model 'SATQuestion'
        db.delete_table('mchlrn_satquestion')

        # Deleting model 'User'
        db.delete_table('mchlrn_user')

        # Deleting model 'Answered_Math_Q'
        db.delete_table('mchlrn_answered_math_q')

        # Deleting model 'Math_Pred'
        db.delete_table('mchlrn_math_pred')

        # Deleting model 'Math_Pred_Row'
        db.delete_table('mchlrn_math_pred_row')

        # Deleting model 'Math_Pred_Item'
        db.delete_table('mchlrn_math_pred_item')

        # Deleting model 'Math_Theta'
        db.delete_table('mchlrn_math_theta')

        # Deleting model 'Math_Theta_Row'
        db.delete_table('mchlrn_math_theta_row')

        # Deleting model 'Math_Theta_Item'
        db.delete_table('mchlrn_math_theta_item')

        # Deleting model 'Math_Q_Processed'
        db.delete_table('mchlrn_math_q_processed')

        # Deleting model 'Math_Q'
        db.delete_table('mchlrn_math_q')

        # Deleting model 'Math_Diagram'
        db.delete_table('mchlrn_math_diagram')

        # Deleting model 'Math_A'
        db.delete_table('mchlrn_math_a')

        # Deleting model 'Math_SP_A'
        db.delete_table('mchlrn_math_sp_a')

        # Deleting model 'Reading_Passage'
        db.delete_table('mchlrn_reading_passage')

        # Deleting model 'Reading_Passage_Q'
        db.delete_table('mchlrn_reading_passage_q')

        # Deleting model 'Reading_Passage_A'
        db.delete_table('mchlrn_reading_passage_a')

        # Deleting model 'Reading_Q'
        db.delete_table('mchlrn_reading_q')

        # Deleting model 'Reading_A'
        db.delete_table('mchlrn_reading_a')

        # Deleting model 'Writing_Passage'
        db.delete_table('mchlrn_writing_passage')

        # Deleting model 'Writing_Passage_Q'
        db.delete_table('mchlrn_writing_passage_q')

        # Deleting model 'Writing_Passage_A'
        db.delete_table('mchlrn_writing_passage_a')

        # Deleting model 'Writing_Effective_Q'
        db.delete_table('mchlrn_writing_effective_q')

        # Deleting model 'Writing_Effective_A'
        db.delete_table('mchlrn_writing_effective_a')

        # Deleting model 'Writing_Grammar_Q'
        db.delete_table('mchlrn_writing_grammar_q')

        # Deleting model 'Writing_Grammar_A'
        db.delete_table('mchlrn_writing_grammar_a')


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
            'difficulty': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'explanation': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructions': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
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