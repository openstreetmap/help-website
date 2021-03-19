+++
type = "question"
title = "MATE: co-relate radius.User_Name and diameter.User-Name messages &amp; extract sessions"
description = '''Hi Experts, Problem statement : I have big trace (&amp;gt;300 MB) which has radius and diameter requests. Username fields in both protocol are common for specific user&#x27;s session lifetime - which I am treating as key for filtering traffic. I want to filter requests wherein I will get complete list (diame...'''
date = "2016-12-19T08:19:00Z"
lastmod = "2016-12-27T07:34:00Z"
weight = 58231
keywords = [ "mate" ]
aliases = [ "/questions/58231" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [MATE: co-relate radius.User\_Name and diameter.User-Name messages & extract sessions](/questions/58231/mate-co-relate-radiususer_name-and-diameteruser-name-messages-extract-sessions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58231-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58231-score" class="post-score" title="current number of votes">0</div><span id="post-58231-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Experts,</p><p>Problem statement : I have big trace (&gt;300 MB) which has radius and diameter requests. Username fields in both protocol are common for specific user's session lifetime - which I am treating as key for filtering traffic. I want to filter requests wherein I will get complete list (diameter and radius) of messages (requests and response) for user's entire session (as long as packets are available in trace :-) )</p><p>I wrote following MATE code :</p><pre><code>Pdu radius_pdu Proto radius Transport ip {
Extract addr From ip.addr ;
Extract port From udp.port ;
Extract radius_id From radius.id ;
Extract username From radius.User_Name ;
Extract radius_code From radius.code ;
};

Gop radius_req On radius_pdu Match (radius_id, addr, addr, port, port) {
Start (radius_code {1|4|40|43} );
Stop (radius_code {2|3|5|41|42|44|45} );
Extra (username);
};

Pdu diameter_pdu Proto diameter Transport ip {
Extract command_code From diameter.cmd.code;
Extract app_id From diameter.applicationId;
Extract session_id From diameter.Session-Id;
Extract username From diameter.User-Name;
Extract e2eid From diameter.endtoendid;
};

Gop dia_tx On diameter_pdu Match (command_code, app_id, session_id, e2eid) {
Start();
Stop(never);
Extra (username);
};

Gog radius_diameter {
Member radius_req(username);
Member dia_tx(username);
Extra (username);
};

Done;</code></pre><p>I tried to apply filters <code>mate.radius_diameter.username == "123456789"</code>. However I am still not able to get expected data. I want to understand if I am missing anything critical or I need to follow some other approach ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mate" rel="tag" title="see questions tagged &#39;mate&#39;">mate</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Dec '16, 08:19</strong></p><img src="https://secure.gravatar.com/avatar/d1e5efe891c907bf6be8231eca9db31a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vijay%20Gharge&#39;s gravatar image" /><p><span>Vijay Gharge</span><br />
<span class="score" title="36 reputation points">36</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vijay Gharge has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Dec '16, 08:22</strong> </span></p></div></div><div id="comments-container-58231" class="comments-container"><span id="58246"></span><div id="comment-58246" class="comment"><div id="post-58246-score" class="comment-score"></div><div class="comment-text"><p>So what kind of data <em>do</em> you get?</p><p>Do the Radius and Diameter parts work independently (i.e., does the Diameter GOP give you all the packets for that user?)?</p><p>In general I'd think what you're trying to do should work. I don't (yet) see what the problem is though...</p></div><div id="comment-58246-info" class="comment-info"><span class="comment-age">(19 Dec '16, 18:50)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="58248"></span><div id="comment-58248" class="comment"><div id="post-58248-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jeff for response.</p><ol><li><p>I can extract diameter / radius messages for specific user i.e. "123456789". However I don't see relevant "response messages" irrespective of radius or diameter. I am not sure what exactly is missing</p></li><li><p>Since there are number of such users - I have to choose 1 user at a time &amp; then apply mate.radius_diameter.username == "$username" filter. This approach just looks impossible. I will have to spend days to filter through complete trace</p></li><li><p>As a end result - I want to extract complete list of messages across radius &amp; diameter - wherein "diameter.Result-Code == 5002"</p></li></ol><p>Kindly guide me through this. Thanks in advance.</p></div><div id="comment-58248-info" class="comment-info"><span class="comment-age">(19 Dec '16, 21:36)</span> <span class="comment-user userinfo">Vijay Gharge</span></div></div></div><div id="comment-tools-58231" class="comment-tools"></div><div class="clear"></div><div id="comment-58231-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58284"></span>

<div id="answer-container-58284" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58284-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58284-score" class="post-score" title="current number of votes">1</div><span id="post-58284-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><ol><li>So if you filter for <code>dia_tx</code> based on username you don't see the Diameter Answers? Looking at what you have there I would expect that to work. I'm not sure what's going on there.</li><li>Well, it depends on what you're trying to do (see next item)...</li><li>So it sounds like you need to add the Diameter Result-Code to the <code>diameter_pdu</code>, then to the <code>dia_tx</code> GOP and then also to the <code>radius_diameter</code> GOG. You /should/ then be able to filter for GOGs that have Result-Code == 5002 which /should/ then show you all the messages in that GOG (Radius and Diameter requests + answers).</li></ol><p>At least that's the theory... Based on my memory... And it's been a while since I've used MATE.</p><p>BTW what version of Wireshark are you using?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Dec '16, 18:51</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-58284" class="comments-container"><span id="58329"></span><div id="comment-58329" class="comment"><div id="post-58329-score" class="comment-score"></div><div class="comment-text"><p>Hi Jeff,</p><p>Thanks for suggestion. I have managed to solve issue partially.</p><p>Following MATE code give me complete life-cycle of the user with few caveat i.e.</p><ol><li>radius request (except CoA) &amp; diameter messages are using IPv6 transport. However Radius CoA message is using IPv4 transport. I am unable to co-relate "radius + coa + diameter" in single MATE filter. Except that all the messages are extracted properly</li><li>I have to go over each and every diameter message which has 5002 Result-Code. Is there any way to get complete list of such messages (having 5002 Result-Code) instead of going over it again and again ? Do I have to use external bash script approach i.e. <code>for loop -&gt; grep -&gt; sort -u</code> ..etc. ?</li></ol><p>Apologies, I couldn't format below message properly hence marked as answer. But voted your earlier message as Solution :-)</p><p>Code :</p><pre><code>Pdu radius_pdu Proto radius Transport ipv6 {
Extract addr From ipv6.addr ;
Extract port From udp.port ;
Extract radius_id From radius.id ;
Extract username From radius.User_Name ;
Extract radius_code From radius.code ;
};

// Identifying PDU start / stop is critical

Gop radius_req On radius_pdu Match (addr, addr, port, port, radius_id ) {
Start (radius_code {1|4} );
Stop (radius_code {2|3|5} );
Extra (username); // This is the common key to link radius &amp; diameter messages
};

Pdu radius_coa_pdu Proto radius Transport udp/ip {
Extract addr From ip.addr ;
Extract port From udp.port ;
Extract radius_id From radius.id ;
Extract username From radius.User_Name ;
Extract radius_code From radius.code ;
};

Gop coa_tx On radius_coa_pdu Match (addr, addr, port, port, radius_id ) {
Start (radius_code {40|43} );
Stop (radius_code {41|42|44|45} );
Extra (username); 
};

Pdu diameter_pdu Proto diameter Transport ip {
Extract command_code From diameter.cmd.code;
Extract app_id From diameter.applicationId;
Extract session_id From diameter.Session-Id;
Extract username From diameter.User-Name;
Extract e2eid From diameter.endtoendid;
Extract diameter_code From diameter.Result-Code ;
};

Gop dia_tx On diameter_pdu Match (command_code, app_id, session_id, e2eid) {
Start();
Stop(never);
Extra (username, diameter_code);
};

// it is critical that both the members on Gog share exactly same key name i.e. username in this case.
// I tried setting one as radius_username &amp; other as diameter_username but I could not filter PDUs with username as key

Gog radius_dia_results {
Member dia_tx(username); 
Member radius_req(username); 
Extra (username, diameter_code); // Extract username field to include in MATE PDU tree
};

Gog coa_dia_results {
Member dia_tx(username); // username is the common key to link radius &amp; diameter messages
Member coa_tx(username); // username is the common key to link radius &amp; diameter messages
Extra (username, diameter_code); // Extract username &amp; diameter_code field to include in MATE PDU tree
};

Done;</code></pre></div><div id="comment-58329-info" class="comment-info"><span class="comment-age">(25 Dec '16, 14:13)</span> <span class="comment-user userinfo">Vijay Gharge</span></div></div><span id="58365"></span><div id="comment-58365" class="comment"><div id="post-58365-score" class="comment-score"></div><div class="comment-text"><p>Glad you're making progress. :-) I converted my comment to an answer your your answer to a comment (more or less as you suggested).</p><p>A note on formatting: yes, I frequently <strong>compose</strong> my <em>comments</em> in the answer window and then cut-n-paste it into the comment window. It makes the formatting easier...</p><ol><li>Two possibilities: a) can you simply change the Radius Transport to <code>udp</code> rather than <code>ip</code> and <code>ipv6</code>? I thought that would work. b) If that doesn't do it can't you add <code>coa_tx(username)</code> to <code>radius_dia_results</code>? A GOG isn't limited to just 2 members and it doesn't (shouldn't) care if the transports are different.</li><li>I assume you're saying that you need to need to look at every message of every group of Radius and Diameter transactions that got a Diameter Result-Code of 5002, presumably one username at a time (i.e., username "12345" got a 5002 so now you need to go look at all the messages <em>for that user</em> leading up to that error)? Yes, I think you're going to have to do that in 2 passes: one to get the list of usernames that got a 5002 and then a second pass to look at the messages for each problematic username. A <code>bash</code>/<code>tshark</code> script would be good for the first pass; how you do the second pass depends on how you want to look at the results. Personally I'd probably do a 2nd pass with <code>tshark</code> generating lots of PCAP files (one per problematic username) so I could view/browser the results in Wireshark.</li></ol></div><div id="comment-58365-info" class="comment-info"><span class="comment-age">(27 Dec '16, 07:34)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-58284" class="comment-tools"></div><div class="clear"></div><div id="comment-58284-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

