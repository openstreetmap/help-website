+++
type = "question"
title = "Wireshark crashes when closing flow graph window"
description = '''Hello: I get a crash of Wireshark 1.1.10 (last stable WinXP 32b version - WinXP 5.1.2600) when I close the &quot;Flow Graph&quot; window, while keeping &quot;Traffic Analysis&quot; window open.  Steps to reproduce it: 1.- Open wireshark and load any trace. 2.- Go to &quot;Statistics&quot; and click on &quot;Flow Graph&quot;.   3.- The &quot;Fl...'''
date = "2013-07-08T13:41:00Z"
lastmod = "2013-07-08T22:20:00Z"
weight = 22734
keywords = [ "crash", "hangs" ]
aliases = [ "/questions/22734" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark crashes when closing flow graph window](/questions/22734/wireshark-crashes-when-closing-flow-graph-window)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22734-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22734-score" class="post-score" title="current number of votes">0</div><span id="post-22734-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello:<br />
I get a crash of Wireshark 1.1.10 (last stable WinXP 32b version - WinXP 5.1.2600) when I close the "Flow Graph" window, while keeping "Traffic Analysis" window open.</p><p>Steps to reproduce it:<br />
1.- Open wireshark and load any trace.</p><p>2.- Go to "Statistics" and click on "Flow Graph".<br />
<img src="https://osqa-ask.wireshark.org/upfiles/statistics-fg-menu.JPG" alt="alt text" /><br />
3.- The "Flow Graph" window will open. Leave all the options by default and click OK.<br />
<img src="https://osqa-ask.wireshark.org/upfiles/flowgraph_window.JPG" alt="alt text" /></p><p>4.- The "Graph Analysis" window will open, like you see below: <img src="https://osqa-ask.wireshark.org/upfiles/graph-analysis-w.JPG" alt="alt text" /></p><p>5.- Now, click on <strong>Close</strong> or <strong>Cancel"</strong> dialogue in the "Flow Graph" window (don't close "Graph Analysis" window)</p><p><img src="https://osqa-ask.wireshark.org/upfiles/close-flow-graph-w.JPG" alt="alt text" /></p><p>6.- Wireshark hangs and get a get crash before some seconds. A window pop up "Wireshark had detected a problem and must be close".<br />
</p><p><img src="https://osqa-ask.wireshark.org/upfiles/ws_crashes.JPG" alt="alt text" /></p><p>With the same trace, in Linux versions, when you execute the step 5, the program close <strong>both window,</strong> but never hangs.</p><p>Thanks for you help or suggestions.</p><p>Miguel Quintana. Support Engineer Sixbell Chile</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-crash" rel="tag" title="see questions tagged &#39;crash&#39;">crash</span> <span class="post-tag tag-link-hangs" rel="tag" title="see questions tagged &#39;hangs&#39;">hangs</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jul '13, 13:41</strong></p><img src="https://secure.gravatar.com/avatar/ddd785174dc48e3284828f386b2082c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mquintanap&#39;s gravatar image" /><p><span>mquintanap</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mquintanap has no accepted answers">0%</span> </br></br></p></img></div></div><div id="comments-container-22734" class="comments-container"></div><div id="comment-tools-22734" class="comment-tools"></div><div class="clear"></div><div id="comment-22734-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="22746"></span>

<div id="answer-container-22746" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22746-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22746-score" class="post-score" title="current number of votes">3</div><span id="post-22746-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sounds like <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8793">bug 8793</a> to me (which will be fixed in 1.10.1 and 1.8.9).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jul '13, 22:20</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span> </br></br></p></img></div></div><div id="comments-container-22746" class="comments-container"></div><div id="comment-tools-22746" class="comment-tools"></div><div class="clear"></div><div id="comment-22746-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22735"></span>

<div id="answer-container-22735" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22735-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22735-score" class="post-score" title="current number of votes">1</div><span id="post-22735-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Great bug report, what is your question? :-)</p><p>This is a Q&amp;A site, where you can ask questions about things you want/need answers to. For bug reports, please file it at <a href="http://bugs.wireshark.org"></a><a href="http://bugs.wireshark.org">http://bugs.wireshark.org</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jul '13, 13:44</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Jul '13, 13:45</strong> </span></p></div></div><div id="comments-container-22735" class="comments-container"><span id="22736"></span><div id="comment-22736" class="comment"><div id="post-22736-score" class="comment-score"></div><div class="comment-text"><p>Hello:</p><p>Really, I don't know if it's a BUG or a problem with my own machine. Before report a BUG, I would like to know if someone knows about this issue, if there's some configuration that I can apply to solve this problem.</p><p>Thanks, Miguel</p></div><div id="comment-22736-info" class="comment-info"><span class="comment-age">(08 Jul '13, 14:10)</span> <span class="comment-user userinfo">mquintanap</span></div></div><span id="22737"></span><div id="comment-22737" class="comment"><div id="post-22737-score" class="comment-score"></div><div class="comment-text"><p>Ok, confirmed, it crashed for me, too. I doubt it is a configuration issue.</p></div><div id="comment-22737-info" class="comment-info"><span class="comment-age">(08 Jul '13, 14:12)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-22735" class="comment-tools"></div><div class="clear"></div><div id="comment-22735-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

