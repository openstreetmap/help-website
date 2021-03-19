+++
type = "question"
title = "DEC to IP Address"
description = '''Hi,  In one of my protocols I receive an integer which represents an ip address. Like this :  180619876... (which means) = AC40A64 = 10.196.10.1 So I would like to have this integer display the ip address. That is, from 180619876 to 10.196.10.1 Is this possible, is there some easy way?  Thank you in...'''
date = "2013-01-17T07:38:00Z"
lastmod = "2013-01-17T12:49:00Z"
weight = 17749
keywords = [ "ip", "dec", "address" ]
aliases = [ "/questions/17749" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [DEC to IP Address](/questions/17749/dec-to-ip-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17749-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>In one of my protocols I receive an integer which represents an ip address. Like this :</p><p>180619876... (which means) = AC40A64 = 10.196.10.1</p><p>So I would like to have this integer display the ip address. That is, from 180619876 to 10.196.10.1</p><p>Is this possible, is there some easy way?</p><p>Thank you in advance,</p><p>BR</p></div><div id="question-tags" class="tags-container tags">ip dec address</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jan '13, 07:38</strong></p><img src="https://secure.gravatar.com/avatar/7709c0c87ed4ba426f119187d3f0c705?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="harkap&#39;s gravatar image" /><p>harkap<br />
<span class="score" title="5 reputation points">5</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="harkap has no accepted answers">0%</span></p></div></div><div id="comments-container-17749" class="comments-container"></div><div id="comment-tools-17749" class="comment-tools"></div><div class="clear"></div><div id="comment-17749-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17754"></span>

<div id="answer-container-17754" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17754-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>In one of <strong>my protocols</strong> I receive an integer</p></blockquote><p>if it's a custom protocol, you need a dissector anyway. Within that code you can do whatever your want, including any number format conversion.</p><p>Some information how to develop a dissector.</p><blockquote><p><a href="http://wiki.wireshark.org/Development">http://wiki.wireshark.org/Development</a><br />
<a href="http://www.wireshark.org/docs/wsdg_html_chunked/">http://www.wireshark.org/docs/wsdg_html_chunked/</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jan '13, 11:03</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Jan '13, 11:04</p></div></div><div id="comments-container-17754" class="comments-container"></div><div id="comment-tools-17754" class="comment-tools"></div><div class="clear"></div><div id="comment-17754-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17761"></span>

<div id="answer-container-17761" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17761-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Is that an integer represented as 4 consecutive bytes (i.e., a binary integer), or is it an integer represented as some number of ASCII characters giving a decimal value? If it's just a binary integer, you could treat it in your dissector as being an IPv4 address type rather than an integer type, the same way a lot of other dissectors (such as, well, the IPv4 dissector) do.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jan '13, 12:49</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-17761" class="comments-container"><span id="17765"></span><div id="comment-17765" class="comment"><div id="post-17765-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>Guy Harris : I think its a binary integer. What I do is that I paste the value in cals, and click hex. The result is AC40A64. Then I just manually look bytewise to get my ip address ( A means 10 , C4 means 196 etc. ).</p><p>Right now the code is</p><p>myprotocol.ip = ProtoField.uint8 ("myproto.ip", "ip")</p><p>and later down :</p><p>subtree:add (myprotocol.ip, buffer(offset, 4))</p><p>Kurt : I already have a dissector dissecting my protocol. The question is now how I can make it display ip address format of this field.</p><p>Thank you for your help</p><p>BR</p></div><div id="comment-17765-info" class="comment-info"><span class="comment-age">(17 Jan '13, 23:38)</span> harkap</div></div><span id="17766"></span><div id="comment-17766" class="comment"><div id="post-17766-score" class="comment-score"></div><div class="comment-text"><p>Spelling error : cals, I mean calc. the windows calculator.</p></div><div id="comment-17766-info" class="comment-info"><span class="comment-age">(17 Jan '13, 23:39)</span> harkap</div></div><span id="17778"></span><div id="comment-17778" class="comment"><div id="post-17778-score" class="comment-score"></div><div class="comment-text"><p>A uint8 field is one byte long; that's not long enough for an IPv4 address.</p><p>Even if it were long enough, by virtue of being a uint32 field, that still wouldn't be treated by Wireshark as an IPv4 address.</p><p>You want to create a field of type ipv4, i.e.</p><pre><code>myprotocol.ip = ProtoField.ipv4(&quot;myproto.ip&quot;, &quot;ip&quot;);</code></pre><p>That field will be displayed as an IPv4 address.</p></div><div id="comment-17778-info" class="comment-info"><span class="comment-age">(18 Jan '13, 10:24)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-17761" class="comment-tools"></div><div class="clear"></div><div id="comment-17761-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

