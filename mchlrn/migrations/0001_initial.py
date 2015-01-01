# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SATQuestion'
        db.create_table(u'mchlrn_satquestion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('answer_A', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('answer_B', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('answer_C', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('answer_D', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('answer_E', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('correct_answer', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('explanation', self.gf('django.db.models.fields.CharField')(max_length=2048, null=True, blank=True)),
            ('instructions', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('channel', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('channel_url', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('difficulty', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('css', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('sub_category', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
        ))
        db.send_create_signal(u'mchlrn', ['SATQuestion'])

        # Adding model 'UserData'
        db.create_table(u'mchlrn_userdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='data', unique=True, to=orm['auth.User'])),
            ('col_num', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'mchlrn', ['UserData'])

        # Adding model 'Answered_Math_Q'
        db.create_table(u'mchlrn_answered_math_q', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('unanswered_q', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mchlrn.Math_Q'], unique=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.UserData'])),
            ('correct', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'mchlrn', ['Answered_Math_Q'])

        # Adding model 'Answered_Sat_Q'
        db.create_table(u'mchlrn_answered_sat_q', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('unanswered_q', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.SATQuestion'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.UserData'])),
            ('correct', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'mchlrn', ['Answered_Sat_Q'])

        # Adding model 'Sat_Pred'
        db.create_table(u'mchlrn_sat_pred', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'mchlrn', ['Sat_Pred'])

        # Adding model 'Sat_Pred_Row'
        db.create_table(u'mchlrn_sat_pred_row', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('row', self.gf('django.db.models.fields.IntegerField')()),
            ('matrix', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.Sat_Pred'])),
        ))
        db.send_create_signal(u'mchlrn', ['Sat_Pred_Row'])

        # Adding model 'Sat_Pred_Item'
        db.create_table(u'mchlrn_sat_pred_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('row', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.Sat_Pred_Row'])),
            ('col', self.gf('django.db.models.fields.IntegerField')()),
            ('val', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'mchlrn', ['Sat_Pred_Item'])

        # Adding model 'Sat_Theta'
        db.create_table(u'mchlrn_sat_theta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'mchlrn', ['Sat_Theta'])

        # Adding model 'Sat_Theta_Row'
        db.create_table(u'mchlrn_sat_theta_row', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('row', self.gf('django.db.models.fields.IntegerField')()),
            ('matrix', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.Sat_Theta'])),
        ))
        db.send_create_signal(u'mchlrn', ['Sat_Theta_Row'])

        # Adding model 'Sat_Theta_Item'
        db.create_table(u'mchlrn_sat_theta_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('row', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.Sat_Theta_Row'])),
            ('col', self.gf('django.db.models.fields.IntegerField')()),
            ('val', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'mchlrn', ['Sat_Theta_Item'])

        # Adding model 'Sat_Q_Processed'
        db.create_table(u'mchlrn_sat_q_processed', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('orig_q', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mchlrn.SATQuestion'], unique=True)),
            ('col_num', self.gf('django.db.models.fields.IntegerField')()),
            ('length', self.gf('django.db.models.fields.IntegerField')()),
            ('num_numbers', self.gf('django.db.models.fields.IntegerField')()),
            ('avg_score', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'mchlrn', ['Sat_Q_Processed'])

        # Adding model 'Math_Pred'
        db.create_table(u'mchlrn_math_pred', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'mchlrn', ['Math_Pred'])

        # Adding model 'Math_Pred_Row'
        db.create_table(u'mchlrn_math_pred_row', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('row', self.gf('django.db.models.fields.IntegerField')()),
            ('matrix', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.Math_Pred'])),
        ))
        db.send_create_signal(u'mchlrn', ['Math_Pred_Row'])

        # Adding model 'Math_Pred_Item'
        db.create_table(u'mchlrn_math_pred_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('row', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.Math_Pred_Row'])),
            ('col', self.gf('django.db.models.fields.IntegerField')()),
            ('val', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'mchlrn', ['Math_Pred_Item'])

        # Adding model 'Math_Theta'
        db.create_table(u'mchlrn_math_theta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'mchlrn', ['Math_Theta'])

        # Adding model 'Math_Theta_Row'
        db.create_table(u'mchlrn_math_theta_row', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('row', self.gf('django.db.models.fields.IntegerField')()),
            ('matrix', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.Math_Theta'])),
        ))
        db.send_create_signal(u'mchlrn', ['Math_Theta_Row'])

        # Adding model 'Math_Theta_Item'
        db.create_table(u'mchlrn_math_theta_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('row', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.Math_Theta_Row'])),
            ('col', self.gf('django.db.models.fields.IntegerField')()),
            ('val', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'mchlrn', ['Math_Theta_Item'])

        # Adding model 'Math_Q_Processed'
        db.create_table(u'mchlrn_math_q_processed', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('orig_q', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mchlrn.Math_Q'], unique=True)),
            ('col_num', self.gf('django.db.models.fields.IntegerField')()),
            ('length', self.gf('django.db.models.fields.IntegerField')()),
            ('num_numbers', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'mchlrn', ['Math_Q_Processed'])

        # Adding model 'Math_Q'
        db.create_table(u'mchlrn_math_q', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=600)),
            ('diagram_exists', self.gf('django.db.models.fields.BooleanField')()),
            ('student_produced', self.gf('django.db.models.fields.BooleanField')()),
            ('a', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('b', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('c', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('d', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'mchlrn', ['Math_Q'])

        # Adding model 'Math_Diagram'
        db.create_table(u'mchlrn_math_diagram', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.Math_Q'])),
            ('diagram', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'mchlrn', ['Math_Diagram'])

        # Adding model 'Math_A'
        db.create_table(u'mchlrn_math_a', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('q', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.Math_Q'])),
            ('answer', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'mchlrn', ['Math_A'])

        # Adding model 'Math_SP_A'
        db.create_table(u'mchlrn_math_sp_a', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('q', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.Math_Q'])),
            ('answer', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'mchlrn', ['Math_SP_A'])

        # Adding model 'Reading_Passage'
        db.create_table(u'mchlrn_reading_passage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('passage', self.gf('django.db.models.fields.CharField')(max_length=10000)),
        ))
        db.send_create_signal(u'mchlrn', ['Reading_Passage'])

        # Adding model 'Reading_Passage_Q'
        db.create_table(u'mchlrn_reading_passage_q', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=600)),
            ('a', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('b', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('c', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('d', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('passage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.Reading_Passage'])),
        ))
        db.send_create_signal(u'mchlrn', ['Reading_Passage_Q'])

        # Adding model 'Reading_Passage_A'
        db.create_table(u'mchlrn_reading_passage_a', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('q', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.Reading_Passage_Q'])),
            ('answer', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'mchlrn', ['Reading_Passage_A'])

        # Adding model 'Reading_Q'
        db.create_table(u'mchlrn_reading_q', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=600)),
            ('a', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('b', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('c', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('d', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'mchlrn', ['Reading_Q'])

        # Adding model 'Reading_A'
        db.create_table(u'mchlrn_reading_a', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('q', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.Reading_Q'])),
            ('answer', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'mchlrn', ['Reading_A'])

        # Adding model 'Writing_Passage'
        db.create_table(u'mchlrn_writing_passage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('passage', self.gf('django.db.models.fields.CharField')(max_length=10000)),
        ))
        db.send_create_signal(u'mchlrn', ['Writing_Passage'])

        # Adding model 'Writing_Passage_Q'
        db.create_table(u'mchlrn_writing_passage_q', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=600)),
            ('a', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('b', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('c', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('d', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('passage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.Writing_Passage'])),
        ))
        db.send_create_signal(u'mchlrn', ['Writing_Passage_Q'])

        # Adding model 'Writing_Passage_A'
        db.create_table(u'mchlrn_writing_passage_a', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('q', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.Writing_Passage_Q'])),
            ('answer', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'mchlrn', ['Writing_Passage_A'])

        # Adding model 'Writing_Effective_Q'
        db.create_table(u'mchlrn_writing_effective_q', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=600)),
            ('underline_start', self.gf('django.db.models.fields.IntegerField')()),
            ('underline_end', self.gf('django.db.models.fields.IntegerField')()),
            ('a', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('b', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('c', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('d', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'mchlrn', ['Writing_Effective_Q'])

        # Adding model 'Writing_Effective_A'
        db.create_table(u'mchlrn_writing_effective_a', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('q', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.Writing_Effective_Q'])),
            ('answer', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'mchlrn', ['Writing_Effective_A'])

        # Adding model 'Writing_Grammar_Q'
        db.create_table(u'mchlrn_writing_grammar_q', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
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
        db.send_create_signal(u'mchlrn', ['Writing_Grammar_Q'])

        # Adding model 'Writing_Grammar_A'
        db.create_table(u'mchlrn_writing_grammar_a', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('q', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mchlrn.Writing_Grammar_Q'])),
            ('answer', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'mchlrn', ['Writing_Grammar_A'])


    def backwards(self, orm):
        # Deleting model 'SATQuestion'
        db.delete_table(u'mchlrn_satquestion')

        # Deleting model 'UserData'
        db.delete_table(u'mchlrn_userdata')

        # Deleting model 'Answered_Math_Q'
        db.delete_table(u'mchlrn_answered_math_q')

        # Deleting model 'Answered_Sat_Q'
        db.delete_table(u'mchlrn_answered_sat_q')

        # Deleting model 'Sat_Pred'
        db.delete_table(u'mchlrn_sat_pred')

        # Deleting model 'Sat_Pred_Row'
        db.delete_table(u'mchlrn_sat_pred_row')

        # Deleting model 'Sat_Pred_Item'
        db.delete_table(u'mchlrn_sat_pred_item')

        # Deleting model 'Sat_Theta'
        db.delete_table(u'mchlrn_sat_theta')

        # Deleting model 'Sat_Theta_Row'
        db.delete_table(u'mchlrn_sat_theta_row')

        # Deleting model 'Sat_Theta_Item'
        db.delete_table(u'mchlrn_sat_theta_item')

        # Deleting model 'Sat_Q_Processed'
        db.delete_table(u'mchlrn_sat_q_processed')

        # Deleting model 'Math_Pred'
        db.delete_table(u'mchlrn_math_pred')

        # Deleting model 'Math_Pred_Row'
        db.delete_table(u'mchlrn_math_pred_row')

        # Deleting model 'Math_Pred_Item'
        db.delete_table(u'mchlrn_math_pred_item')

        # Deleting model 'Math_Theta'
        db.delete_table(u'mchlrn_math_theta')

        # Deleting model 'Math_Theta_Row'
        db.delete_table(u'mchlrn_math_theta_row')

        # Deleting model 'Math_Theta_Item'
        db.delete_table(u'mchlrn_math_theta_item')

        # Deleting model 'Math_Q_Processed'
        db.delete_table(u'mchlrn_math_q_processed')

        # Deleting model 'Math_Q'
        db.delete_table(u'mchlrn_math_q')

        # Deleting model 'Math_Diagram'
        db.delete_table(u'mchlrn_math_diagram')

        # Deleting model 'Math_A'
        db.delete_table(u'mchlrn_math_a')

        # Deleting model 'Math_SP_A'
        db.delete_table(u'mchlrn_math_sp_a')

        # Deleting model 'Reading_Passage'
        db.delete_table(u'mchlrn_reading_passage')

        # Deleting model 'Reading_Passage_Q'
        db.delete_table(u'mchlrn_reading_passage_q')

        # Deleting model 'Reading_Passage_A'
        db.delete_table(u'mchlrn_reading_passage_a')

        # Deleting model 'Reading_Q'
        db.delete_table(u'mchlrn_reading_q')

        # Deleting model 'Reading_A'
        db.delete_table(u'mchlrn_reading_a')

        # Deleting model 'Writing_Passage'
        db.delete_table(u'mchlrn_writing_passage')

        # Deleting model 'Writing_Passage_Q'
        db.delete_table(u'mchlrn_writing_passage_q')

        # Deleting model 'Writing_Passage_A'
        db.delete_table(u'mchlrn_writing_passage_a')

        # Deleting model 'Writing_Effective_Q'
        db.delete_table(u'mchlrn_writing_effective_q')

        # Deleting model 'Writing_Effective_A'
        db.delete_table(u'mchlrn_writing_effective_a')

        # Deleting model 'Writing_Grammar_Q'
        db.delete_table(u'mchlrn_writing_grammar_q')

        # Deleting model 'Writing_Grammar_A'
        db.delete_table(u'mchlrn_writing_grammar_a')


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
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'data'", 'unique': 'True', 'to': u"orm['auth.User']"})
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