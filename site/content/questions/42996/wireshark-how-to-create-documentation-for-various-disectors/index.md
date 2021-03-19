+++
type = "question"
title = "WireShark : How to create documentation for various Disectors"
description = '''Hello, I wanted to create documentation for various specs, something like  a) PDU Header and port  b) What are the message type  c)Information present in each message type   b1) its type (ie simple (int,bit,long,etc) or complex (if complex   define childs for it)   b2) length   Idea is to have somet...'''
date = "2015-06-08T23:31:00Z"
lastmod = "2015-06-09T03:57:00Z"
weight = 42996
keywords = [ "dissector" ]
aliases = [ "/questions/42996" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [WireShark : How to create documentation for various Disectors](/questions/42996/wireshark-how-to-create-documentation-for-various-disectors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42996-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42996-score" class="post-score" title="current number of votes">0</div><span id="post-42996-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I wanted to create documentation for various specs, something like</p><pre><code>a) PDU Header and port   
b) What are the message type    
c)Information present in each message type   
   b1) its type (ie simple (int,bit,long,etc) or complex (if complex 
       define childs for it)  
   b2) length</code></pre><p>Idea is to have something like WSGD (wireshark Generic Dissector ) document , so its easy to understand specs internal. Though information is present in either 3GPP word document but its not computer friendly.</p><p>Any suggestions on how I can create it are most welcome (Right now I am parsing the word document to get tables from it, but again it wont work for all specs). If something like this is already existing , please do point.</p><p>Initially I want to work on all LTE related specs (NAS, Diameter, RTP, SIP etc) , but then I will create for all dissectors.</p><p>regards</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jun '15, 23:31</strong></p><img src="https://secure.gravatar.com/avatar/3d041dad7dade4fc0aeeb32031c0e191?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bhardwaj_rajesh&#39;s gravatar image" /><p><span>bhardwaj_rajesh</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bhardwaj_rajesh has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Jun '15, 02:27</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-42996" class="comments-container"><span id="43011"></span><div id="comment-43011" class="comment"><div id="post-43011-score" class="comment-score"></div><div class="comment-text"><p>I think rather than trying to infer from the source file, it'd be easier to extract some of this information from a running instance of Wireshark (or tshark). Have you seen what's available in the 'Internals' menu?</p></div><div id="comment-43011-info" class="comment-info"><span class="comment-age">(09 Jun '15, 03:57)</span> <span class="comment-user userinfo">MartinM</span></div></div></div><div id="comment-tools-42996" class="comment-tools"></div><div class="clear"></div><div id="comment-42996-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43004"></span>

<div id="answer-container-43004" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43004-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43004-score" class="post-score" title="current number of votes">0</div><span id="post-43004-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Woa... nice <strong>LITTLE</strong> project ;-)</p><p>The idea, to have a protocol definition in a WSGD like format is good, but I don't see how this can be extracted from the Wireshark code. Seriously, I don't see <strong>any</strong> easy way (or any way at all) to compile a WSGD like protocol definition by reading ("dissecting") the Wireshark source code, neither manually nor by using any tool (script). This task would be way to complex to be worth the effort.</p><p>You could check the Microsoft Network Monitor Parsers. They use their own definition language for the parsers (their form of dissectors). The parsers are open source and do contain a lot of common protocols.</p><blockquote><p><a href="http://www.codeplex.com/NMParsers">http://www.codeplex.com/NMParsers</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jun '15, 02:38</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-43004" class="comments-container"></div><div id="comment-tools-43004" class="comment-tools"></div><div class="clear"></div><div id="comment-43004-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

