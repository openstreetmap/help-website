+++
type = "question"
title = "GLib Thread not initialized"
description = '''Hi there, I download the 1.6.3 source package, compile and install went OK, but on execution I&#x27;ve got an error raising from GLib : GLib-ERROR **: The thread system is not yet initialized. aborting... Can anyone help... seems to be a GLib problem rather than Wiresharks... does glib require some intia...'''
date = "2011-11-14T08:54:00Z"
lastmod = "2011-11-15T08:45:00Z"
weight = 7416
keywords = [ "glib", "threads" ]
aliases = [ "/questions/7416" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [GLib Thread not initialized](/questions/7416/glib-thread-not-initialized)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7416-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>I download the 1.6.3 source package, compile and install went OK, but on execution I've got an error raising from GLib :</p><p>GLib-ERROR **: The thread system is not yet initialized. aborting...</p><p>Can anyone help... seems to be a GLib problem rather than Wiresharks... does glib require some intialization or so ? do I need glib-devel package ?</p><p>Thanks !</p><p>Tips: I've got a 2.6.17 kernel from Mandriva with glib version 2.0.0.1200.11 installed</p></div><div id="question-tags" class="tags-container tags">glib threads</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Nov '11, 08:54</strong></p><img src="https://secure.gravatar.com/avatar/50fb2b078363521170dab88586426792?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wirebilly&#39;s gravatar image" /><p>wirebilly<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wirebilly has 2 accepted answers">66%</span></p></div></div><div id="comments-container-7416" class="comments-container"></div><div id="comment-tools-7416" class="comment-tools"></div><div class="clear"></div><div id="comment-7416-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="7447"></span>

<div id="answer-container-7447" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7447-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I applied the two patches.</p><p>Alas, there is still something wrong with the build system. I don't know libtool at all. Since this is a new problem I make a new forum entry and consider this one solved.</p><p>Thanks again for your help.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Nov '11, 08:45</strong></p><img src="https://secure.gravatar.com/avatar/50fb2b078363521170dab88586426792?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wirebilly&#39;s gravatar image" /><p>wirebilly<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wirebilly has 2 accepted answers">66%</span></p></div></div><div id="comments-container-7447" class="comments-container"></div><div id="comment-tools-7447" class="comment-tools"></div><div class="clear"></div><div id="comment-7447-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7417"></span>

<div id="answer-container-7417" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7417-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I suspect this is related to http://wiki.wireshark.org/Development/Roadmap</p><p>Rev 38045, Rev 38046 - Bug 6540 - Don't use g_mutex without having threads.</p><p>try applying thos two patches.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '11, 09:15</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-7417" class="comments-container"></div><div id="comment-tools-7417" class="comment-tools"></div><div class="clear"></div><div id="comment-7417-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

