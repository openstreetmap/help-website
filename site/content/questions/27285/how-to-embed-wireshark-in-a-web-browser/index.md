+++
type = "question"
title = "How to embed wireshark in a web browser"
description = '''I would like to embed wireshark in a web browser in order to view message exchange on my webpage (running on a local machine) with packet filtering. The basic aim is to integrate Operations and Management Webpage which controls a LTE eNodeB &amp;amp; wireshark.'''
date = "2013-11-22T09:25:00Z"
lastmod = "2013-11-23T09:24:00Z"
weight = 27285
keywords = [ "embed", "firefox", "lte" ]
aliases = [ "/questions/27285" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to embed wireshark in a web browser](/questions/27285/how-to-embed-wireshark-in-a-web-browser)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27285-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to embed wireshark in a web browser in order to view message exchange on my webpage (running on a local machine) with packet filtering.</p><p>The basic aim is to integrate Operations and Management Webpage which controls a LTE eNodeB &amp; wireshark.</p></div><div id="question-tags" class="tags-container tags">embed firefox lte</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Nov '13, 09:25</strong></p><img src="https://secure.gravatar.com/avatar/c85bdd524a63219d456fe36d7a5979cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anish&#39;s gravatar image" /><p>Anish<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anish has no accepted answers">0%</span></p></div></div><div id="comments-container-27285" class="comments-container"></div><div id="comment-tools-27285" class="comment-tools"></div><div class="clear"></div><div id="comment-27285-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="27287"></span>

<div id="answer-container-27287" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27287-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Take a look at <a href="http://www.cloushark.org">http://www.cloushark.org</a></p><blockquote><p><a href="http://www.cloudshark.org/captures/f62e1db77ba0">http://www.cloudshark.org/captures/f62e1db77ba0</a></p></blockquote><p>If you want to know how <strong>that</strong> works, please contact the guys at cloudshark.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Nov '13, 09:38</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-27287" class="comments-container"><span id="27288"></span><div id="comment-27288" class="comment"><div id="post-27288-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt</p><p>However, using cloudshark.org, I can only view my capture files on a web browser.</p><p>My intent is to have some what like a wireshark plugin for firefox or any other browser using which I can perform live capture and the same would be embedded in my OAM webpage.</p><p>Regards Anish</p></div><div id="comment-27288-info" class="comment-info"><span class="comment-age">(22 Nov '13, 09:59)</span> Anish</div></div><span id="27291"></span><div id="comment-27291" class="comment"><div id="post-27291-score" class="comment-score"></div><div class="comment-text"><p>as you may know, Wireshark is a <strong>Desktop GUI application</strong>. There is <strong>no way</strong> to simply 'embed' it into a web browser or a web application (hosted on a web server). Maybe it's easier to understand if you try to simply 'embed' your favorite Windows GUI application (editor, etc.) in a web browser/application? How would you do that? No way.</p><p>That's the reason why I pointed you to cloudshark. The guys over there seem to use tshark (a CLI tool) to extract data from a capture file. Then they wrote some code to view that data in a nice looking web application.</p><p>And that's basically what you'll have to do as well. Additionally you can implement the data capturing part, that's currently missing in cloudshark. You can do that by calling dumpcap.</p><p><strong>BUT</strong>, don't expect to get all that done on a Wednesday afternoon. I guess the development of cloudshark took several months, if not years.</p><p>However, I might have misunderstood what you are trying to do. If so, please be more specific on that part.</p></div><div id="comment-27291-info" class="comment-info"><span class="comment-age">(22 Nov '13, 11:34)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-27287" class="comment-tools"></div><div class="clear"></div><div id="comment-27287-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="27301"></span>

<div id="answer-container-27301" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27301-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>How to embed Wireshark in a web page? Rewrite the UI so that it's a web-page. There was a proposal to do that as part of the Google Summer of Code 2013 but the <a href="http://wiki.wireshark.org/GSoC2013#JSONshark">project</a> didn't go anywhere (that I know of).</p><p>(In other words, what you're proposing is a significant if not massive project.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Nov '13, 09:24</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-27301" class="comments-container"><span id="27304"></span><div id="comment-27304" class="comment"><div id="post-27304-score" class="comment-score"></div><div class="comment-text"><p>I wonder if it would be possible to build a (usable) GUI with one of the new HTML5 frameworks, that promise cross-platform development of 'GUI applications', even for the Desktop.</p><blockquote><p><a href="http://www.kendoui.com/">http://www.kendoui.com/</a><br />
<a href="http://www.tidesdk.org/">http://www.tidesdk.org/</a><br />
<a href="http://webix.com/">http://webix.com/</a><br />
<a href="http://www.zebkit.com/">http://www.zebkit.com/</a></p></blockquote><p>A pure web application, hosted on a server, might not be 'responsive' enough (see cloudshark.org). However, the same thing on the Desktop could probably work.</p><p>Anyone ever thought about that as an option (instead of Qt)?</p></div><div id="comment-27304-info" class="comment-info"><span class="comment-age">(23 Nov '13, 13:17)</span> Kurt Knochner ♦</div></div><span id="27305"></span><div id="comment-27305" class="comment"><div id="post-27305-score" class="comment-score"></div><div class="comment-text"><p>There's still the issue of the non-gui major part of Wireshark, the dissectors. They are built as a platform specific native code library. The html5 JavaScript GUI will have to call and interact with that.</p></div><div id="comment-27305-info" class="comment-info"><span class="comment-age">(23 Nov '13, 14:10)</span> grahamb ♦</div></div><span id="27306"></span><div id="comment-27306" class="comment"><div id="post-27306-score" class="comment-score"></div><div class="comment-text"><p>Well, the thing is <strong>not</strong> to rewrite everything in Javascript, 'just' to replace the UI part with 'something' based on HTML5. I know that's not easy (maybe not possible at all), but it's also a lot of work to migrate to Qt.</p><p>I just wonder if anyone of you guys has some experience with this and can estimate if it is possible at all, or if there is a major show stopper (except the amount of work to do, more like the ever changing browser engines and bugs introduced with those changes). I have not really looked into those HTML5 toolkits to do that estimation by myself.</p></div><div id="comment-27306-info" class="comment-info"><span class="comment-age">(23 Nov '13, 14:48)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-27301" class="comment-tools"></div><div class="clear"></div><div id="comment-27301-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

