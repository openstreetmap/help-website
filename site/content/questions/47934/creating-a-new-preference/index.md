+++
type = "question"
title = "Creating a new preference"
description = '''I am trying to create a new preference under Edit -&amp;gt; Preferences -&amp;gt; User Interface. I can create the text field, but when I fill it with text nothing else happens. When I click apply or ok, and reopen the window, the text is gone. When I grep through the .wireshark/preferences file, I don&#x27;t se...'''
date = "2015-11-24T11:31:00Z"
lastmod = "2015-11-25T14:56:00Z"
weight = 47934
keywords = [ "development", "gtk", "preferences" ]
aliases = [ "/questions/47934" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Creating a new preference](/questions/47934/creating-a-new-preference)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47934-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47934-score" class="post-score" title="current number of votes">0</div><span id="post-47934-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to create a new preference under Edit -&gt; Preferences -&gt; User Interface. I can create the text field, but when I fill it with text nothing else happens. When I click apply or ok, and reopen the window, the text is gone. When I grep through the .wireshark/preferences file, I don't see the value I entered.<br />
</p><p>I have made the following changes to ui/gtk/prefs_gui.c</p><pre><code> #define GUI_MYTEST_DIR_KEY     &quot;path_directory&quot;
...
 GtkWidget *my_test_path_te;
...
    /* Testing my text edit preference */
    my_test_path_te = create_preference_entry(main_grid, pos++,
        &quot;My Test Path:&quot;,
        &quot;The Location of something I want.&quot;,
        prefs.mypath_dir); //created this variable in prefs.h
    g_object_set_data(G_OBJECT(main_vb), GUI_MYTEST_DIR_KEY, my_test_path_te);
...
    prefs.mypath_dir = g_strdup(gtk_entry_get_text(
          GTK_ENTRY(g_object_get_data(G_OBJECT(w), GUI_MYTEST_DIR_KEY))));</code></pre><p>Did I miss something with what I tried? My ultimate goal is to have the new preference pass in a string that will be sent to a few different dissectors.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-gtk" rel="tag" title="see questions tagged &#39;gtk&#39;">gtk</span> <span class="post-tag tag-link-preferences" rel="tag" title="see questions tagged &#39;preferences&#39;">preferences</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Nov '15, 11:31</strong></p><img src="https://secure.gravatar.com/avatar/b7abadc19faf42f27c2c2feeae249e1f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="0xbismarck&#39;s gravatar image" /><p><span>0xbismarck</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="0xbismarck has one accepted answer">100%</span> </br></p></div></div><div id="comments-container-47934" class="comments-container"></div><div id="comment-tools-47934" class="comment-tools"></div><div class="clear"></div><div id="comment-47934-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47997"></span>

<div id="answer-container-47997" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47997-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47997-score" class="post-score" title="current number of votes">0</div><span id="post-47997-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="0xbismarck has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Had to play with the code a while, but I finally figured it out.</p><p>Here is the list of changes I had to make to get it to write to file and show up in the GUI.</p><p>epan/prefs.h in e_prefs add:</p><pre><code>  gchar       *mypath_dir;</code></pre><p>epan/prefs.c</p><pre><code>prefs_register_directory_preference(gui_module, &quot;mytest.dir&quot;, &quot;New Test&quot;,
        &quot;This test better work&quot;, (const char **)&amp;prefs.mypath_dir);</code></pre><p>ui/gtk/pref_gui.c</p><pre><code>static gboolean mytest_changed_cb(GtkWidget *myentry _U_, GdkEvent *event _U_, gpointer parent_w);
...
#define GUI_MYTEST_DIR_KEY      &quot;path_directory&quot;
...</code></pre><p>within gui_prefs_show() GtkWidget *my_test_path_te;</p><pre><code>...
    my_test_path_te = create_preference_entry(main_grid, pos++,
        &quot;My Test Path:&quot;,
        &quot;The Location of something I want.&quot;,
        prefs.mypath_dir);
    g_object_set_data(G_OBJECT(main_vb), GUI_MYTEST_DIR_KEY, my_test_path_te);
    g_signal_connect(my_test_path_te, &quot;focus_out_event&quot;, G_CALLBACK(mytest_changed_cb), main_vb);
    printf(&quot;my new function&quot;, prefs.mypath_dir);</code></pre><p>within gui_prefs_fetch():</p><pre><code>prefs.mypath_dir = g_strdup(gtk_entry_get_text(
              GTK_ENTRY(g_object_get_data(G_OBJECT(w), GUI_MYTEST_DIR_KEY))));

static gboolean
mytest_changed_cb(GtkWidget *recent_files_entry _U_,
          GdkEvent *event _U_, gpointer parent_w)
{
    GtkWidget   *recent_files_count_te;
    gchar * newval;

    recent_files_count_te = (GtkWidget *)g_object_get_data(G_OBJECT(parent_w), GUI_MYTEST_DIR_KEY);

    strlen(gtk_entry_get_text (GTK_ENTRY(recent_files_count_te)));
    newval = gtk_entry_get_text (GTK_ENTRY(recent_files_count_te));

    prefs.mypath_dir = newval;

    return FALSE;
}</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '15, 14:56</strong></p><img src="https://secure.gravatar.com/avatar/b7abadc19faf42f27c2c2feeae249e1f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="0xbismarck&#39;s gravatar image" /><p><span>0xbismarck</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="0xbismarck has one accepted answer">100%</span></p></div></div><div id="comments-container-47997" class="comments-container"></div><div id="comment-tools-47997" class="comment-tools"></div><div class="clear"></div><div id="comment-47997-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

