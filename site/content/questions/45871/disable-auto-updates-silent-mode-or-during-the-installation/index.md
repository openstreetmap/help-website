+++
type = "question"
title = "Disable auto-updates - silent mode or during the installation"
description = '''Hi guys, In my company, we are managing software and patches by Kace. So I need to disable WireShark auto-updates of all machines, remotely.  There is an option[parameter] to put during the installation or something I can do to disable the auto updates? --  I created a GPO that changes a registry ke...'''
date = "2015-09-16T01:56:00Z"
lastmod = "2015-09-16T02:53:00Z"
weight = 45871
keywords = [ "installation", "updates", "silent" ]
aliases = [ "/questions/45871" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Disable auto-updates - silent mode or during the installation](/questions/45871/disable-auto-updates-silent-mode-or-during-the-installation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45871-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45871-score" class="post-score" title="current number of votes">0</div><span id="post-45871-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys,</p><p>In my company, we are managing software and patches by Kace. So I need to disable WireShark auto-updates of all machines, remotely.</p><p>There is an option[parameter] to put during the installation or something I can do to disable the auto updates?</p><p>-- I created a GPO that changes a registry key to turn off autoup dates for Wireshark:</p><pre><code>Hive    Key Path    Value Name  Value Type  Value Data  Base</code></pre><p>Wireshark HKEY_CURRENT_USER Software\Wireshark\WinSparkle Settings CheckForUpdates REG_DWORD 00000000 Hexadecimal</p><p>The registry has been modified ok in my computer so the GPO works. However I still see a pop up window when I start Wireshark saying there is a new version available. This only happens the first time I open it… Then it doesn’t happen until I open it again the next day or after a while…</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-updates" rel="tag" title="see questions tagged &#39;updates&#39;">updates</span> <span class="post-tag tag-link-silent" rel="tag" title="see questions tagged &#39;silent&#39;">silent</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Sep '15, 01:56</strong></p><img src="https://secure.gravatar.com/avatar/a97f3dc11b666b3d9b4b0392f155ccd8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="coxadoido&#39;s gravatar image" /><p><span>coxadoido</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="coxadoido has no accepted answers">0%</span></p></div></div><div id="comments-container-45871" class="comments-container"></div><div id="comment-tools-45871" class="comment-tools"></div><div class="clear"></div><div id="comment-45871-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45873"></span>

<div id="answer-container-45873" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45873-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45873-score" class="post-score" title="current number of votes">0</div><span id="post-45873-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>When looking at Wireshark source code, I can see that it activates the automatic update in WinSparkle configuration based on the gui.update.enabled parameter found in the %APPDATA%\Wireshark\preferences file. This will change the CheckForUpdates registry setting.</p><p>Right now we do not have an installer switch making it configurable. Moreover the Wireshark preferences file is not created until the program is launched for the first time. So it's kind of egg and chicken problem. And changing the registry key will not prevent the user from launching manually an update verification through the web GUI.</p><p>You might want to fill an enhancement bug to <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> to have this functionality integrated in a future release. For now the only way would be to recompile and distribute Wireshark without the auto updater feature.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Sep '15, 02:53</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-45873" class="comments-container"></div><div id="comment-tools-45873" class="comment-tools"></div><div class="clear"></div><div id="comment-45873-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

