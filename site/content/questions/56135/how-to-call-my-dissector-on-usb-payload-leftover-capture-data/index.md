+++
type = "question"
title = "How to call my dissector on USB payload (leftover capture data)"
description = '''Hello, in the question How can I decrypt SSL session with Lua dissector, a custom Lua dissector is added to the dissector table &quot;usb.bulk&quot;. My usecase is similar: I need to dissect a proprietary protocol on top of the USB protocol. But the following instruction (as seen in that question) doesn&#x27;t see...'''
date = "2016-10-04T07:40:00Z"
lastmod = "2016-10-05T02:48:00Z"
weight = 56135
keywords = [ "lua", "dissector", "usb" ]
aliases = [ "/questions/56135" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to call my dissector on USB payload (leftover capture data)](/questions/56135/how-to-call-my-dissector-on-usb-payload-leftover-capture-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56135-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56135-score" class="post-score" title="current number of votes">0</div><span id="post-56135-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>in the question <a href="https://ask.wireshark.org/questions/56115/how-can-i-decrypt-ssl-session-with-lua-dissector">How can I decrypt SSL session with Lua dissector</a>, a custom Lua dissector is added to the dissector table "usb.bulk". My usecase is similar: I need to dissect a proprietary protocol on top of the USB protocol. But the following instruction (as seen in that question) doesn't seem to do the trick:</p><pre><code>function myprotocol.init()
    DissectorTable.get(&quot;usb.bulk&quot;):add(0xFF, myprotocol)
end</code></pre><p>Normally I would replace the dissector with my own, keeping a reference to the original one and call that explicitly if needed (like described <a href="https://ask.wireshark.org/questions/54870/how-to-register-a-lua-dissector-for-8021q-ethernet-payload">here</a>) - but I do not know which dissector(s) from that DissectorTable I need to replace. So I am stuck with the following questions:</p><ol><li>What is the behavior of a DissectorTable when I add another dissector? What do I have to do so that my dissector gets called?</li><li>Which dissectors are contained in the usb.bulk DissectorTable? I could not find out on github (btw. I am not a C programmer)</li><li>Does the 'pattern' argument of the <a href="https://wiki.wireshark.org/LuaAPI/Dissector#dissectortable:add.28pattern.2C_dissector.29">add</a> function (the value 0xFF in this case) have any relevance for USB dissector tables?</li><li>Should I create my own DissectorTable for this usecase? Why would I need one?</li></ol><p>Any help is much appreciated. Thank you in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-usb" rel="tag" title="see questions tagged &#39;usb&#39;">usb</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Oct '16, 07:40</strong></p><img src="https://secure.gravatar.com/avatar/00a96bd28fd02417186122229a517000?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="patrick_oppermann&#39;s gravatar image" /><p><span>patrick_oppe...</span><br />
<span class="score" title="46 reputation points">46</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="patrick_oppermann has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Oct '16, 07:44</strong> </span></p></div></div><div id="comments-container-56135" class="comments-container"></div><div id="comment-tools-56135" class="comment-tools"></div><div class="clear"></div><div id="comment-56135-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56136"></span>

<div id="answer-container-56136" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56136-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56136-score" class="post-score" title="current number of votes">1</div><span id="post-56136-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="patrick_oppermann has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Handling of USB captures is a bit complex in terms that the possibility to choose a dissector for the payload automatically often depends on whether the enumeration phase has been captured or not, because the "integer" dissector tables refer to values of fields of USB descriptors which are only transferred over the bus during the enumeration phase.</p><p>So in the particular case of that other Question, the <code>0xff</code> (or 255) value inserted into the <code>usb.bulk</code> <strong>integer</strong> dissector table probably matches the value of <code>bInterfaceClass</code> from the interface descriptor. That table is, as its name suggests, only consulted for USB <strong>bulk</strong> transfers.</p><p>For payloads which follow some characteristic patterns, the choice of dissector is slightly easier, because it is possible to use heuristic to choose the proper dissector even if the enumeration phase is missing in the capture. A heuristic dissector also needs to be registered for a transport protocol, and all heuristic dissectors registered for a given transport are tried on all payload PDUs of that transport until one of them succeeds, with the following exception: if a heuristic dissector for protocol X succeeds on a PDU, it may declare that PDU to be part of a "conversation" of protocol X; doing so makes the transport protocol's dissector invoke the dissector for protocol X on further PDUs with identical address attributes (in our case, the USB address <code>B.D.E</code> - Bus.Device.Endpoint) directly rather than attempt all registered heuristic dissectors again. So for USB bulk transfers, you would register your protocol's heuristic dissector as one for transport <code>usb.bulk</code>. I'm simplifying here a bit because I don't know whether you actually need the details.</p><p>So the first things to do for you is to check what type of USB transfer your proprietary protocol is using, whether the pattern is unambiguous enough that it would be safe to base a heuristic on it. If you cannot rely on heuristic and the transfer used is bulk, find out what <code>bInterfaceClass</code> value your USB device is sending in its <code>GET DESCRIPTOR Response CONFIGURATION</code> answer during enumeration phase. For other transfer types, another field of another message may have been chosen as selector.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Oct '16, 09:06</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Oct '16, 09:10</strong> </span></p></div></div><div id="comments-container-56136" class="comments-container"><span id="56149"></span><div id="comment-56149" class="comment"><div id="post-56149-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your profound answer! It was the 'bInterfaceClass' field I was looking for. When I add my dissector to the dissector table with the value that my capture data contains (0xffff), it gets called properly! If I need to distinguish between different message types, I can ask the development team to provide more specific values for bInterfaceClass.</p><p>In combination with 'usb.transfer_type', this already solves my problem, so there is no need for me to write a heuristic dissector (which would have been rather difficult for my protocol, anyway).</p></div><div id="comment-56149-info" class="comment-info"><span class="comment-age">(05 Oct '16, 02:48)</span> <span class="comment-user userinfo">patrick_oppe...</span></div></div></div><div id="comment-tools-56136" class="comment-tools"></div><div class="clear"></div><div id="comment-56136-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

