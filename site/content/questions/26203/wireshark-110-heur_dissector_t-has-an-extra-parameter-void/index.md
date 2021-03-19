+++
type = "question"
title = "Wireshark 1.10 heur_dissector_t has an extra parameter void*"
description = '''I have a plugin dissector and I&#x27;m upgrading to 1.10.  I ran across a compile warning where the definition of heur_dissector_t now has an extra parameter void* The header file doesn&#x27;t have any documentation for the parameter. What is it for? I grepped the other plugins and see that packet-esl.c as we...'''
date = "2013-10-18T15:23:00Z"
lastmod = "2013-10-18T17:16:00Z"
weight = 26203
keywords = [ "heur_dissector_add", "plugin" ]
aliases = [ "/questions/26203" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark 1.10 heur\_dissector\_t has an extra parameter void\*](/questions/26203/wireshark-110-heur_dissector_t-has-an-extra-parameter-void)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26203-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a plugin dissector and I'm upgrading to 1.10.<br />
</p><p>I ran across a compile warning where the definition of heur_dissector_t now has an extra parameter void* The header file doesn't have any documentation for the parameter. What is it for?</p><p>I grepped the other plugins and see that packet-esl.c as well as all the others that have heur_dissector_add which doesn't have the 4th parameter void*</p></div><div id="question-tags" class="tags-container tags">heur_dissector_add plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Oct '13, 15:23</strong></p><img src="https://secure.gravatar.com/avatar/0b4ddeb095ff16e8a84fe92d03bbdef4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tlann&#39;s gravatar image" /><p>tlann<br />
<span class="score" title="76 reputation points">76</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tlann has 4 accepted answers">100%</span> </br></p></div></div><div id="comments-container-26203" class="comments-container"></div><div id="comment-tools-26203" class="comment-tools"></div><div class="clear"></div><div id="comment-26203-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26205"></span>

<div id="answer-container-26205" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26205-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>What is it for?</p></blockquote><p>Passing private data from one dissector to another, rather than using the <code>pinfo-&gt;private_data</code> mechanism (if it's passed as an argument, you don't have to worry about overwriting somebody else's private data pointer). If you have no extra data to pass to a dissector, pass NULL; if you have no extra data to be passed to you, ignore the argument (and mark it with <code>_U_</code> so that the compiler doesn't warn you it's unused).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '13, 17:16</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-26205" class="comments-container"><span id="26262"></span><div id="comment-26262" class="comment"><div id="post-26262-score" class="comment-score"></div><div class="comment-text"><p>Is there an example of how this is used in the source?</p></div><div id="comment-26262-info" class="comment-info"><span class="comment-age">(21 Oct '13, 15:41)</span> tlann</div></div></div><div id="comment-tools-26205" class="comment-tools"></div><div class="clear"></div><div id="comment-26205-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

