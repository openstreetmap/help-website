+++
type = "question"
title = "How to setup and run tshark on OS X 10.9.2"
description = '''Hello there, I would like to how to run tshark on OS X 10.9.2. I installed Wireshark 1.10.5 on my OS X. and tried to find tshark command using spotlight. but I can not find it. Could you tell me how to setup it on OS X 10.9.2? Thank you.'''
date = "2014-03-15T10:52:00Z"
lastmod = "2014-03-15T11:19:00Z"
weight = 30819
keywords = [ "osx", "wireshark" ]
aliases = [ "/questions/30819" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to setup and run tshark on OS X 10.9.2](/questions/30819/how-to-setup-and-run-tshark-on-os-x-1092)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30819-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30819-score" class="post-score" title="current number of votes">0</div><span id="post-30819-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello there, I would like to how to run tshark on OS X 10.9.2. I installed Wireshark 1.10.5 on my OS X. and tried to find tshark command using spotlight. but I can not find it. Could you tell me how to setup it on OS X 10.9.2? Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Mar '14, 10:52</strong></p><img src="https://secure.gravatar.com/avatar/25297a2bff646a4d876c5f83fb3b081f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Juza&#39;s gravatar image" /><p><span>Juza</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Juza has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Mar '14, 10:53</strong> </span></p></div></div><div id="comments-container-30819" class="comments-container"></div><div id="comment-tools-30819" class="comment-tools"></div><div class="clear"></div><div id="comment-30819-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30820"></span>

<div id="answer-container-30820" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30820-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30820-score" class="post-score" title="current number of votes">0</div><span id="post-30820-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It should be installed in <code>/usr/local/bin</code>, so running it from the commandline (in a terminal shell) should just work:</p><pre><code>tshark -v</code></pre><p>If it doesn't, then see if it's not there: <code>ls /usr/local/bin</code>, and if it is there then your PATH environment variable might not have that directory.</p><p>If it's not there, and not in some other root <code>bin</code> directory, then you can copy it from the installed application package - it will be in <code>/Applications/Wireshark.app/Contents/MacOS/</code>. But I think it would be a bug if it weren't installed in <code>/usr/local/bin</code> or some root directory in your PATH, so post back here if it's not.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '14, 11:19</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-30820" class="comments-container"></div><div id="comment-tools-30820" class="comment-tools"></div><div class="clear"></div><div id="comment-30820-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

