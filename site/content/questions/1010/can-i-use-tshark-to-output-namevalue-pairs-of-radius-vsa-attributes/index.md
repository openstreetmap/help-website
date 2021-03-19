+++
type = "question"
title = "Can I use tshark to output name/value pairs of Radius VSA attributes?"
description = '''When decoding RADIUS traffic, wireshark displays Attribute Value Pairs in a format such as:  + AVP: l=22 t=user-Name(1): username@address  + AVP: l=17 t=Calling-Station-Id(31): ABCDEFG etc. Is there a way to use tshark to output these name value pairs as text? e.g.  row 1 user-name username@address ...'''
date = "2010-11-18T07:52:00Z"
lastmod = "2010-11-20T03:02:00Z"
weight = 1010
keywords = [ "tshark" ]
aliases = [ "/questions/1010" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Can I use tshark to output name/value pairs of Radius VSA attributes?](/questions/1010/can-i-use-tshark-to-output-namevalue-pairs-of-radius-vsa-attributes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1010-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When decoding RADIUS traffic, wireshark displays Attribute Value Pairs in a format such as: + AVP: l=22 t=user-Name(1): [email protected] + AVP: l=17 t=Calling-Station-Id(31): ABCDEFG</p><p>etc.</p><p>Is there a way to use tshark to output these name value pairs as text?</p><p>e.g. row 1 user-name [email protected] Calling-Station-Id ABCDEFG</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Nov '10, 07:52</strong></p><img src="https://secure.gravatar.com/avatar/bddcc1f355a85cf062d811abe24cd285?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mlampell&#39;s gravatar image" /><p>mlampell<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mlampell has no accepted answers">0%</span></p></div></div><div id="comments-container-1010" class="comments-container"></div><div id="comment-tools-1010" class="comment-tools"></div><div class="clear"></div><div id="comment-1010-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1031"></span>

<div id="answer-container-1031" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1031-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Or you can use tshark with the "-T fields" option to extract the fields of interest:</p><pre><code>$ tshark -nlr RADIUS.cap -R &quot;radius.code == 1&quot; -T fields \
     -e frame.time -e radius.User_Name -e radius.Calling_Station_Id
Aug  2, 2008 00:52:17.872968000 John.McGuirk    00-14-22-E9-54-5E
Aug  2, 2008 00:52:17.916736000 John.McGuirk    00-14-22-E9-54-5E
$</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '10, 03:02</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-1031" class="comments-container"><span id="1166"></span><div id="comment-1166" class="comment"><div id="post-1166-score" class="comment-score"></div><div class="comment-text"><p>thanks SYNbit, your answer works very well.</p></div><div id="comment-1166-info" class="comment-info"><span class="comment-age">(29 Nov '10, 14:06)</span> mlampell</div></div></div><div id="comment-tools-1031" class="comment-tools"></div><div class="clear"></div><div id="comment-1031-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1011"></span>

<div id="answer-container-1011" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1011-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>tshark does show the AVP name/value pairs if you show the packet details using the -V switch. However it also shows all the packet details. :)</p><p>You can use grep (or something similar) to filter for just the name/value lines from the tshark output; Does this meet your needs ?</p><p>tshark -nVr &lt;filename&gt; | grep "AVP:"</p><pre><code>   AVP: l=6  t=Service-Type(6): Framed(2)
   AVP: l=6  t=Framed-Protocol(7): GPRS-PDP-Context(7)
   AVP: l=12  t=Vendor-Specific(26) v=3GPP(10415)
   AVP: l=6  t=NAS-Port-Type(61): Virtual(5)
   AVP: l=4  t=User-Name(1): aj
   AVP: l=19  t=CHAP-Password(3): 012b9d0750c7de94e99492fbe8083e3dbc
   AVP: l=22  t=CHAP-Challenge(60): 7eca5d703bf5d617ef9746349ab0adc93c400ad4
   AVP: l=6  t=NAS-IP-Address(4): 10.147.4.165
   AVP: l=6  t=NAS-Port(5): 99996
   AVP: l=6  t=Framed-IP-Address(8): 10.146.8.251
   AVP: l=15  t=Calling-Station-Id(31): 8613505619900
   AVP: l=7  t=Called-Station-Id(30): cmwap</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Nov '10, 08:28</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Nov '10, 08:40</p></div></div><div id="comments-container-1011" class="comments-container"><span id="1012"></span><div id="comment-1012" class="comment"><div id="post-1012-score" class="comment-score"></div><div class="comment-text"><p>The above was done using tshark -nVr &lt;filename&gt; | grep "AVP:"</p></div><div id="comment-1012-info" class="comment-info"><span class="comment-age">(18 Nov '10, 08:29)</span> Bill Meier ♦♦</div></div><span id="1013"></span><div id="comment-1013" class="comment"><div id="post-1013-score" class="comment-score"></div><div class="comment-text"><p>Bill, that's a great suggestion, thanks. I had not known there was a way to output the entire decoded text. Thanks.</p></div><div id="comment-1013-info" class="comment-info"><span class="comment-age">(18 Nov '10, 08:37)</span> mlampell</div></div><span id="1014"></span><div id="comment-1014" class="comment"><div id="post-1014-score" class="comment-score"></div><div class="comment-text"><p>(I've changed your "answer" to to be a "comment" in keeping with the way this site works; The FAQ gives more info).</p></div><div id="comment-1014-info" class="comment-info"><span class="comment-age">(18 Nov '10, 08:47)</span> Bill Meier ♦♦</div></div></div><div id="comment-tools-1011" class="comment-tools"></div><div class="clear"></div><div id="comment-1011-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

