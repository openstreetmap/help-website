+++
type = "question"
title = "Protocol analyzer for validating custom network protocol"
description = '''I have a server and a client that are sending binary data inside custom structured TCP/UDP packets (a pretty standard scenario I&#x27;m sure). In order to validate the data, I would like to use Wireshark to check that the packet structure and contents are correct, but want to avoid the current necessity ...'''
date = "2014-11-19T18:31:00Z"
lastmod = "2014-11-25T17:03:00Z"
weight = 37986
keywords = [ "lua", "dissector", "protocol", "network", "analysis" ]
aliases = [ "/questions/37986" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Protocol analyzer for validating custom network protocol](/questions/37986/protocol-analyzer-for-validating-custom-network-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37986-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37986-score" class="post-score" title="current number of votes">0</div><span id="post-37986-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a server and a client that are sending binary data inside custom structured TCP/UDP packets (a pretty standard scenario I'm sure). In order to validate the data, I would like to use Wireshark to check that the packet structure and contents are correct, but want to avoid the current necessity of (for example) finding the 16-19th bytes in packetX and converting that 32 bit float to a decimal, or scrolling down to the 2314th byte in packetY to see if that byte is 03 or 04 is what's causing the bug... etc etc.</p><p>I know wireshark has built-in decoders for a huge variety of common protocols (e.g. HTTP), but what is the best way forward for analyzing custom byte packets (incl variable length)? The packets I am looking at all have a header with a magic start, length, name, and a magic end.</p><p>An Lua dissector looks like the right tool, but before I jump into it, I want to see what others might recommend or suggest?</p><p><strong>/edit:</strong> Real-time is preferred. I am not looking to capture and analyze later, so if I am using Wireshark, I want to see the dissected packets as they come in, and even filter by packet names I have pre-defined in my Lua (if this is possible?)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span> <span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '14, 18:31</strong></p><img src="https://secure.gravatar.com/avatar/33446b713282cb77d176fc09465801aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fidelius&#39;s gravatar image" /><p><span>Fidelius</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fidelius has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Nov '14, 18:37</strong> </span></p></div></div><div id="comments-container-37986" class="comments-container"></div><div id="comment-tools-37986" class="comment-tools"></div><div class="clear"></div><div id="comment-37986-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37999"></span>

<div id="answer-container-37999" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37999-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37999-score" class="post-score" title="current number of votes">1</div><span id="post-37999-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Fidelius has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A Lua dissector is one option. Please see the docs and samples to get started.</p><p>Another option is the Wireshark gerneric dissector (third party add-on).</p><blockquote><p><a href="http://wsgd.free.fr/">http://wsgd.free.fr/</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '14, 01:33</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-37999" class="comments-container"><span id="38007"></span><div id="comment-38007" class="comment"><div id="post-38007-score" class="comment-score">1</div><div class="comment-text"><p>Shameless plug, see my <a href="http://sharkfest.wireshark.org/assets/presentations13/PA-10_Writing-a-Wireshark-Dissector_Graham-Bloice.zip">presentation</a> and other materials from Sharkfest'13 about writing a dissector that covers a basic dissector using WSGD, Lua and C.</p></div><div id="comment-38007-info" class="comment-info"><span class="comment-age">(20 Nov '14, 02:20)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="38010"></span><div id="comment-38010" class="comment"><div id="post-38010-score" class="comment-score"></div><div class="comment-text"><p>+1</p><p>no need to be "ashamed" ;-)</p></div><div id="comment-38010-info" class="comment-info"><span class="comment-age">(20 Nov '14, 02:52)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="38011"></span><div id="comment-38011" class="comment"><div id="post-38011-score" class="comment-score"></div><div class="comment-text"><p>I'm not, hence the "shameless" :-)</p></div><div id="comment-38011-info" class="comment-info"><span class="comment-age">(20 Nov '14, 02:56)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="38148"></span><div id="comment-38148" class="comment"><div id="post-38148-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt. I started using WSGD but decided the build-in support that Wireshark has for Lua is preferred to a third party dll which might stop development at any stage. And grahamb, that link is dead but I found your zip at <a href="http://sharkfest.wireshark.org/sharkfest.13/presentations/PA-10_Writing-a-Wireshark-Dissector_Graham-Bloice.zip">http://sharkfest.wireshark.org/sharkfest.13/presentations/PA-10_Writing-a-Wireshark-Dissector_Graham-Bloice.zip</a> Very useful thank you!</p></div><div id="comment-38148-info" class="comment-info"><span class="comment-age">(25 Nov '14, 17:03)</span> <span class="comment-user userinfo">Fidelius</span></div></div></div><div id="comment-tools-37999" class="comment-tools"></div><div class="clear"></div><div id="comment-37999-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

