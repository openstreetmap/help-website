+++
type = "question"
title = "How to also filter out responses?"
description = '''Hi All, !radius.Framed-IP-Address!=x.x.x.x filters out all RADIUS Acct requests (UDP) with Framed-IP-Address AVP = anything but x.x.x.x. How do I also filter out their respective responses (ACK/NAK) that carry no such AVP? Many thanks in advance, Dmitriy'''
date = "2014-09-19T13:30:00Z"
lastmod = "2014-10-21T05:55:00Z"
weight = 36470
keywords = [ "radius" ]
aliases = [ "/questions/36470" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to also filter out responses?](/questions/36470/how-to-also-filter-out-responses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36470-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36470-score" class="post-score" title="current number of votes">0</div><span id="post-36470-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>!radius.Framed-IP-Address!=x.x.x.x filters out all RADIUS Acct requests (UDP) with Framed-IP-Address AVP = anything but x.x.x.x. How do I also filter out their respective responses (ACK/NAK) that carry no such AVP?</p><p>Many thanks in advance,</p><p>Dmitriy</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-radius" rel="tag" title="see questions tagged &#39;radius&#39;">radius</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Sep '14, 13:30</strong></p><img src="https://secure.gravatar.com/avatar/4c43e04f0ef8eacb2a3173436cb432f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dmitriy&#39;s gravatar image" /><p><span>Dmitriy</span><br />
<span class="score" title="21 reputation points">21</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dmitriy has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Sep '14, 15:24</strong> </span></p></div></div><div id="comments-container-36470" class="comments-container"><span id="36561"></span><div id="comment-36561" class="comment"><div id="post-36561-score" class="comment-score"></div><div class="comment-text"><p>... sorry, if it's a well known question a link to the answer would really help as I didn't come across any.</p><p>Many thanks in advance,</p><p>Dmitriy</p></div><div id="comment-36561-info" class="comment-info"><span class="comment-age">(24 Sep '14, 06:47)</span> <span class="comment-user userinfo">Dmitriy</span></div></div></div><div id="comment-tools-36470" class="comment-tools"></div><div class="clear"></div><div id="comment-36470-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37197"></span>

<div id="answer-container-37197" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37197-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37197-score" class="post-score" title="current number of votes">2</div><span id="post-37197-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Dmitriy has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can't really do this kind of thing just with display filters. But you could build a <a href="http://wiki.wireshark.org/Mate">MATE</a> configuration file which effectively copies the Framed-IP-Address into the response message and then filter based on the new (MATE-based) field.</p><p>Unfortunately the documentation on the wiki is hopelessly out of date so this may be hard to achieve but it is possible.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '14, 06:05</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-37197" class="comments-container"><span id="37199"></span><div id="comment-37199" class="comment"><div id="post-37199-score" class="comment-score"></div><div class="comment-text"><p>Hi Jeff,</p><p>Thanks for your reply. Sounds like the ACKs that survive such filtering will also have that AVP added? If so I hope there's also a way of removing that AVP from them afterwards, perhaps also using MATE... problem is the traces we collect are an evidence of testing and so altering them except for filtering out unrelated traffic is generally not a very good thing to do (at least altering the contents of individual packets).</p><p>Do you think adding something like a special keyword or character into the display filter line to easily tell Wireshark "and their respective responses" could qualify as an enhancement request? I do understand it's unlikely to be a top priority one.</p><p>Many thanks,</p><p>Dmitriy</p></div><div id="comment-37199-info" class="comment-info"><span class="comment-age">(20 Oct '14, 06:28)</span> <span class="comment-user userinfo">Dmitriy</span></div></div><span id="37200"></span><div id="comment-37200" class="comment"><div id="post-37200-score" class="comment-score"></div><div class="comment-text"><p>Sorry, my answer was confusing.</p><p>MATE won't actually modify the messages at all. But it will create "meta" fields which are present on all frames that are in a Group Of Packets (gop). So you wouldn't end up filtering for "radius.Framed-IP-Address" but something more like "mate.MyRadiusThingy.Framed-IP-Address" (I don't have a MATE configuration loaded at the moment so the actual syntax will likely be different).</p><p>To make things easier, here's a MATE configuration file I sometimes use with Diameter:</p><pre><code>// A Wireshark MATE configuration file to identify Diameter transactions.

// Create a &quot;diam_pdu&quot; that contains various pieces of the processed Diameter
// message.
Pdu diam_pdu Proto diameter Transport ip {
        Extract command_code From diameter.cmd.code;
        Extract app_id From diameter.applicationId;
        Extract session_id From diameter.Session-Id;
        Extract imsi From diameter.User-Name;
        Extract e2eid From diameter.endtoendid;
};

// Then create a GOP (Group Of Pdus) where the each GOP contains all the PDUs
// (msgs) that whose command_code, app_id, session_id, and e2eid match.
Gop diam_transaction On diam_pdu Match (command_code, app_id, session_id, e2eid) {
        Start();
        Stop(never);

        // Store the IMSI in the GOP
        Extra(imsi);
};

Done;</code></pre></div><div id="comment-37200-info" class="comment-info"><span class="comment-age">(20 Oct '14, 06:46)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="37204"></span><div id="comment-37204" class="comment"><div id="post-37204-score" class="comment-score"></div><div class="comment-text"><p>I've just tried this one:</p><pre><code>Pdu rad_pdu Proto radius Transport ip {
    Extract framed_ip_address From radius.Framed-IP-Address;
    Extract packet_id From radius.id;

};

Gop rad_transaction On rad_pdu Match (framed_ip_address) {
    Start();
    Stop(never);

    Extra(packet_id);
};

Done;</code></pre><p>Each packet now has additional MATE level under RADIUS. However when I try filtering using mate.rad_pdu.framed_ip_address==10.0.2.4 or mate.rad_transaction.framed_ip_address==10.0.2.4 I can see no packets at all. If I just apply mate.rad_pdu.framed_ip_address or mate.rad_transaction.framed_ip_address see all requests (any IP) but no responses. Is it correct behaviour?</p><p>My Wireshark is Version 1.12.2rc0-32-gce0e169 (v1.12.2rc0-32-gce0e169 from master-1.12).</p></div><div id="comment-37204-info" class="comment-info"><span class="comment-age">(20 Oct '14, 10:46)</span> <span class="comment-user userinfo">Dmitriy</span></div></div><span id="37211"></span><div id="comment-37211" class="comment"><div id="post-37211-score" class="comment-score"></div><div class="comment-text"><p>OK, it's getting better: seems like all MATE values must be in quotes, e.g. this one works: mate.rad_pdu.framed_ip_address=="10.0.2.4" and so does this one: "mate.rad_transaction.framed_ip_address=="10.0.2.4". Still they only allow requests carrying that IP and not their respective ACKs. If however I try filtering on packet_id that is present in both requests and ACKs it effectively becomes a manual operation while the goal is to make it automatically filter all packets with packet_id value pertaining to a call with a desired IP address.</p></div><div id="comment-37211-info" class="comment-info"><span class="comment-age">(20 Oct '14, 16:17)</span> <span class="comment-user userinfo">Dmitriy</span></div></div><span id="37216"></span><div id="comment-37216" class="comment"><div id="post-37216-score" class="comment-score"></div><div class="comment-text"><p>I see a couple problems, hopefully fixing these will get it working.</p><p>1) You don't want the Gop to match on framed_ip_address: the problem you're trying to solve is that the responses don't have that AVP so with that <code>match</code> you'll never build a Gop that includes a response. I don't know Radius but I'm guessing packet_id is what allows you to match the response to the request. So: you want to <code>match</code> the packet_id.</p><p>2) Then, to actually copy the framed_ip_address into the Gop you want <code>Extra(framed_ip_address)</code> in the Gop definition.</p></div><div id="comment-37216-info" class="comment-info"><span class="comment-age">(21 Oct '14, 00:54)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="37221"></span><div id="comment-37221" class="comment not_top_scorer"><div id="post-37221-score" class="comment-score"></div><div class="comment-text"><p>After swapping around framed_ip_address and packet_id in rad_transaction it works a treat: as you said IP address can now be found in MATE layer of both requests and responses indeed, so display filter line "!mate.rad_transaction.framed_ip_address!="10.0.2.4"" filters out everything but requests and responses for that IP. It even handles PoD (Disconnect requests and ACK) messages properly whenever they're present.</p><p>Perfect - thank you so much! It's a shame to learn about so powerful tools after so much time wasted doing the same manually... still better late than never )</p></div><div id="comment-37221-info" class="comment-info"><span class="comment-age">(21 Oct '14, 03:22)</span> <span class="comment-user userinfo">Dmitriy</span></div></div><span id="37226"></span><div id="comment-37226" class="comment not_top_scorer"><div id="post-37226-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-37226-info" class="comment-info"><span class="comment-age">(21 Oct '14, 04:00)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="37235"></span><div id="comment-37235" class="comment not_top_scorer"><div id="post-37235-score" class="comment-score"></div><div class="comment-text"><p>Sure - done.</p></div><div id="comment-37235-info" class="comment-info"><span class="comment-age">(21 Oct '14, 05:55)</span> <span class="comment-user userinfo">Dmitriy</span></div></div></div><div id="comment-tools-37197" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-37197-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

