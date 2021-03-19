+++
type = "question"
title = "Getting R6034 runtime error while opening any trace file"
description = '''Hi Folks, I had made a dissector plugin some time back with VS 2008 and Wireshark 1.7.1. It used to run fine with version-1.7.1 but same plugin gives me &quot;R6034 runtime error&quot; with Wireshark 1.8.2 ,which happens to be latest stable release. Now i found this thread below , wherein it is mentioned that...'''
date = "2012-08-20T08:11:00Z"
lastmod = "2012-08-20T08:53:00Z"
weight = 13755
keywords = [ "plugin", "visual-studio", "wireshark" ]
aliases = [ "/questions/13755" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Getting R6034 runtime error while opening any trace file](/questions/13755/getting-r6034-runtime-error-while-opening-any-trace-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13755-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Folks,</p><p>I had made a dissector plugin some time back with VS 2008 and Wireshark 1.7.1.</p><p>It used to run fine with version-1.7.1 but same plugin gives me "R6034 runtime error" with Wireshark 1.8.2 ,which happens to be latest stable release.</p><p>Now i found this thread below , wherein it is mentioned that VS version should be same for plugin and executable. Now i wanted to know which VS version was used to build 1.8.2 ?? And how can i make my plugin compatible with both release ?</p><blockquote><blockquote><p><a href="http://www.wireshark.org/lists/wireshark-dev/201004/msg00302.html">http://www.wireshark.org/lists/wireshark-dev/201004/msg00302.html</a></p></blockquote></blockquote></div><div id="question-tags" class="tags-container tags">plugin visual-studio wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Aug '12, 08:11</strong></p><img src="https://secure.gravatar.com/avatar/d15cd2870e25518ba76d2eb42f56bbcb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yogeshg&#39;s gravatar image" /><p>yogeshg<br />
<span class="score" title="41 reputation points">41</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yogeshg has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Aug '12, 08:11</p></div></div><div id="comments-container-13755" class="comments-container"></div><div id="comment-tools-13755" class="comment-tools"></div><div class="clear"></div><div id="comment-13755-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13758"></span>

<div id="answer-container-13758" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13758-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Now i wanted to know which VS version was used to build 1.8.2</p></blockquote><p>This command will tell you:</p><blockquote><p><code>wireshark -v</code><br />
</p></blockquote><p>Look for "Built using Microsoft Visual C++ ....".</p><blockquote><p>And how can i make my plugin compatible with both release ?</p></blockquote><p>Please read the following questions/answers.</p><blockquote><p><code>http://ask.wireshark.org/questions/12706/custom-dissector-portability</code><br />
<code>http://ask.wireshark.org/questions/13484/dll-not-working-with-wireshark-181</code><br />
<code>http://ask.wireshark.org/questions/13594/updating-my-own-plugin</code><br />
</p></blockquote><p>AFIAK it's not possible to make your plugin compatible with both releases.</p><p>You could write an installer, that determines the wireshark version and then installs the appropriate plugin, OR you distribute your plugin together with the wireshark version it needs.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Aug '12, 08:53</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Aug '12, 08:54</p></div></div><div id="comments-container-13758" class="comments-container"><span id="13760"></span><div id="comment-13760" class="comment"><div id="post-13760-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply sir!!</p><p>It shows -- "Built using Microsoft Visual C++ 10.0 build 40219"</p><p>I think this is the reason of my problem.</p></div><div id="comment-13760-info" class="comment-info"><span class="comment-age">(20 Aug '12, 09:04)</span> yogeshg</div></div><span id="13761"></span><div id="comment-13761" class="comment"><div id="post-13761-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I think this is the reason of my problem.</p></blockquote><p>it is ;-)</p></div><div id="comment-13761-info" class="comment-info"><span class="comment-age">(20 Aug '12, 09:05)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-13758" class="comment-tools"></div><div class="clear"></div><div id="comment-13758-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

