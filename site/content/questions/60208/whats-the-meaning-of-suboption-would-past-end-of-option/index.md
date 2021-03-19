+++
type = "question"
title = "What&#x27;s the meaning of &#x27;Suboption would past end of option&#x27;?"
description = '''I want IP Options to record route data,so I modified an ping packet&#x27;s IP Options. Then I sent it and captured it use wireshark to see whether it worked. I found there is no right response but I received another packets. The packets I sent and I received as follows：   So I want to know what&#x27;s wrong w...'''
date = "2017-03-20T22:06:00Z"
lastmod = "2017-03-21T03:21:00Z"
weight = 60208
keywords = [ "ip" ]
aliases = [ "/questions/60208" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What's the meaning of 'Suboption would past end of option'?](/questions/60208/whats-the-meaning-of-suboption-would-past-end-of-option)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60208-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want IP Options to record route data,so I modified an ping packet's IP Options. Then I sent it and captured it use wireshark to see whether it worked. I found there is no right response but I received another packets. The packets I sent and I received as follows：</p><p><img src="https://s29.postimg.org/n7w48iq6t/image.jpg" alt="The packet that I sent" /></p><p><img src="https://s23.postimg.org/fcpj2bg8r/image.jpg" alt="The packet that I received" /></p><p>So I want to know what's wrong with it.</p></div><div id="question-tags" class="tags-container tags">ip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Mar '17, 22:06</strong></p><img src="https://secure.gravatar.com/avatar/c357860459dd25fcc4ec19d50221fcdd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zhao&#39;s gravatar image" /><p>Zhao<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zhao has no accepted answers">0%</span></p></img></div></div><div id="comments-container-60208" class="comments-container"></div><div id="comment-tools-60208" class="comment-tools"></div><div class="clear"></div><div id="comment-60208-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60217"></span>

<div id="answer-container-60217" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60217-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>what's wrong with it.</p></blockquote><p>The length of the Record Route option is incorrect.</p><p>As <a href="https://tools.ietf.org/html/rfc791">RFC 791</a>, "Internet Protocol", says on page 15, "The option-length octet counts the option-type octet and the option-length octet as well as the option-data octets." The description of the Record Route option begins on page 20; that option has 1 byte of option type, 1 byte of option length, 1 byte of pointer, and a sequence of 4-byte IPv4 addresses.</p><p>The length in your Record Route option is 40. The first 3 of those 40 bytes are the option type, option length, and pointer; that leaves 37 bytes of IPv4 addresses, which is not valid, because that's not a multiple of 4. There are 9 IPv4 addresses in the option, so that's 36 bytes of IPv4 addresses, so the option length should be 39, not 40. Nowhere in RFC 791 does it say that the <em>option length</em> must be a multiple of 4 bytes; in fact, it shows that the length of the Security option must be 11, which is not only not a multiple of 4, it's not a multiple of anything other than 11 and 1, being a prime number.</p><p>The expert info should be attached to the option length, or to the extra byte of option, not to the pointer, as the pointer field is valid.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '17, 03:21</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></img></div></div><div id="comments-container-60217" class="comments-container"></div><div id="comment-tools-60217" class="comment-tools"></div><div class="clear"></div><div id="comment-60217-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

