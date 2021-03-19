+++
type = "question"
title = "Plugin - dlg_utils in dissector"
description = '''I&#x27;ve been trying to incorporate some GUI utils in a dissector which is being developed as a plugin for Wireshark. The functionalities I need are the ones declared in ui/gtk/dlg_utils.h, specially the function dlg_window_new. I have linked libgtkui.lib (also present in ui/gtk) in the relevant Makefil...'''
date = "2013-09-25T01:51:00Z"
lastmod = "2013-09-25T16:43:00Z"
weight = 25189
keywords = [ "gui", "dissector", "plugin" ]
aliases = [ "/questions/25189" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Plugin - dlg\_utils in dissector](/questions/25189/plugin-dlg_utils-in-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25189-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25189-score" class="post-score" title="current number of votes">0</div><span id="post-25189-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been trying to incorporate some GUI utils in a dissector which is being developed as a plugin for Wireshark. The functionalities I need are the ones declared in <strong>ui/gtk/dlg_utils.h</strong>, specially the function <strong>dlg_window_new</strong>. I have linked <strong>libgtkui.lib</strong> (also present in <strong>ui/gtk</strong>) in the relevant Makefile, but this library apparently requires the linkage of many other ones. Should <strong>libgtkui.lib</strong> be kind of stand-alone? If it should, what's been done wrong? If it should not, which other libraries must be linked with it?</p><p>Thanks in advance!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gui" rel="tag" title="see questions tagged &#39;gui&#39;">gui</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Sep '13, 01:51</strong></p><img src="https://secure.gravatar.com/avatar/b15e02964ce3e65a7e667354809a33e5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Matheus%20Priebe%20Bertram&#39;s gravatar image" /><p><span>Matheus Prie...</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Matheus Priebe Bertram has one accepted answer">100%</span></p></div></div><div id="comments-container-25189" class="comments-container"></div><div id="comment-tools-25189" class="comment-tools"></div><div class="clear"></div><div id="comment-25189-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25191"></span>

<div id="answer-container-25191" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25191-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25191-score" class="post-score" title="current number of votes">0</div><span id="post-25191-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Matheus Priebe Bertram has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>GUI stuff in dissectors isn't supported as they must also be able to run from the command line with tshark, see <a href="http://ask.wireshark.org/questions/8848/message-box-from-dissector-plugin">this</a> question for more info.</p><p>What exactly are you trying to do as there may be a more suitable way to achieve it?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '13, 02:08</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Sep '13, 02:09</strong> </span></p></div></div><div id="comments-container-25191" class="comments-container"><span id="25195"></span><div id="comment-25195" class="comment"><div id="post-25195-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the prompt answer. I have registered a uat preference for the dissector and get some relevant data from there. The table is, in a first instance, empty. In this sense, I wanted to add a functionality to load default preferences into this table e.g. by clicking a button such as "Load default table". The button thing, however, wouldn't work. Therefore, I tried to create a new dialogue window to ask the user, when deleting an item from the table, if the current desire is loading the default table (i.e. deleting all entries) or just deleting the selected entry.</p><p>As I can see in the referenced post, that is not practicable. I've already come across things such as "report_failure", but I'd actually need a dialogue.</p><p>I guess the correct way would be registering one of the supported preference types (like a boolean value) which dictates the functioning of the preferences table.</p></div><div id="comment-25195-info" class="comment-info"><span class="comment-age">(25 Sep '13, 02:28)</span> <span class="comment-user userinfo">Matheus Prie...</span></div></div><span id="25250"></span><div id="comment-25250" class="comment"><div id="post-25250-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Therefore, I tried to create a new dialogue window to ask the user, when deleting an item from the table, if the current desire is loading the default table (i.e. deleting all entries) or just deleting the selected entry.</p></blockquote><p>This suggests that there should, in the UI for UAT preferences, be a "revert to default" option. (There might be a <em>global</em> "revert to default" option that reverts <em>all</em> preferences, but that's presumably too much for what you want.)</p></div><div id="comment-25250-info" class="comment-info"><span class="comment-age">(25 Sep '13, 16:43)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-25191" class="comment-tools"></div><div class="clear"></div><div id="comment-25191-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

