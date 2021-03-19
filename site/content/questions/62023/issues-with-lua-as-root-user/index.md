+++
type = "question"
title = "Issues with Lua as root user"
description = '''Hi, I am a new user to wireshark and I just recently compiled wireshark from sources. However, I am facing an issue. Wireshark is not starting up with Lua capability (unable to view it under Tools-&amp;gt;Lua) I did the following steps:  downloaded lua to directory under /usr/local/&amp;lt;lua-5.1&amp;gt;  buil...'''
date = "2017-06-14T09:54:00Z"
lastmod = "2017-07-05T10:28:00Z"
weight = 62023
keywords = [ "lua" ]
aliases = [ "/questions/62023" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Issues with Lua as root user](/questions/62023/issues-with-lua-as-root-user)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62023-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62023-score" class="post-score" title="current number of votes">0</div><span id="post-62023-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am a new user to wireshark and I just recently compiled wireshark from sources. However, I am facing an issue.</p><p>Wireshark is not starting up with Lua capability (unable to view it under Tools-&gt;Lua) I did the following steps:</p><ol><li>downloaded lua to directory under /usr/local/&lt;lua-5.1&gt;</li><li>built lua using "make linux test"</li><li>Downloaded wireshark 2.2.7</li><li>Did "configure --with-lua" //seems to be working fine.</li><li>Did "make" //runs fine , no errors</li></ol><p>I also viewed the "About" section when wireshark starts and I am able to see "built with Lua-5.1" But I am very puzzled and perplexed as to why it doesnt show up under "Tools -&gt; Lua"</p><p>Also, on another machine, I did this as a non root user and I am able to see Tools-&gt;Lua, but the interfaces for packet capture do not show up (probably since this requires root permissions)</p><p>I would be grateful if someone could kindly help me out</p><p>regards TJ</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jun '17, 09:54</strong></p><img src="https://secure.gravatar.com/avatar/976233ee489208b9373f8a4d4df9733e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tharamur&#39;s gravatar image" /><p><span>tharamur</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tharamur has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Jun '17, 10:22</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-62023" class="comments-container"></div><div id="comment-tools-62023" class="comment-tools"></div><div class="clear"></div><div id="comment-62023-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62033"></span>

<div id="answer-container-62033" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62033-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62033-score" class="post-score" title="current number of votes">0</div><span id="post-62033-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>By default Lua scripts will not be executed if Wireshark is running as the root user. The theory there is that running Wireshark's 2+ million lines of code as root is bad enough but running scripts would be even worse.</p><p>I would very strongly suggest you configure things so you don't have to run Wireshark as root. <a href="https://blog.wireshark.org/2010/02/running-wireshark-as-you/">Gerald's blog post</a> has an excellent description; you'll also find <a href="https://ask.wireshark.org/questions/7976/wireshark-setup-linux-for-nonroot-user">answers</a> on this site on how to do it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jun '17, 13:29</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-62033" class="comments-container"><span id="62535"></span><div id="comment-62535" class="comment"><div id="post-62535-score" class="comment-score"></div><div class="comment-text"><p>Hi Jeff</p><p>Thanks a lot for your reply...I'm sorry I couldn't get back sooner, as I was temporarily assigned to another project.</p><p>Btw, I tried out the remedies suggested by you, but then the same issue persists When wireshark starts up as non root, none of the interfaces get displayed.</p><p>Is there any other way to resolve the issue ?</p><p>regards Tej</p></div><div id="comment-62535-info" class="comment-info"><span class="comment-age">(05 Jul '17, 09:29)</span> <span class="comment-user userinfo">tharamur</span></div></div><span id="62536"></span><div id="comment-62536" class="comment"><div id="post-62536-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-62536-info" class="comment-info"><span class="comment-age">(05 Jul '17, 09:37)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="62539"></span><div id="comment-62539" class="comment"><div id="post-62539-score" class="comment-score"></div><div class="comment-text"><p>Which method did you use to run Wireshark as non-root (there are a couple alternatives outlined in Gerald's blog post)?</p></div><div id="comment-62539-info" class="comment-info"><span class="comment-age">(05 Jul '17, 10:28)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-62033" class="comment-tools"></div><div class="clear"></div><div id="comment-62033-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

