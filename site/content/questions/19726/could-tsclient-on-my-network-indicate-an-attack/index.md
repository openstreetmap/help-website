+++
type = "question"
title = "Could &quot;tsclient&quot; on my network indicate an attack?"
description = '''&quot;tsclient&quot; recently appeared on a Windows 8 machine we have on our network. Reading around, it sounds like this is typically used for remote desktop applications. However, I haven&#x27;t used any remote desktop services. (Unless some indirect application uses them? xbox glass?) Could the appearance of ts...'''
date = "2013-03-21T11:49:00Z"
lastmod = "2013-03-21T18:13:00Z"
weight = 19726
keywords = [ "tsclient", "attack", "investigate" ]
aliases = [ "/questions/19726" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Could "tsclient" on my network indicate an attack?](/questions/19726/could-tsclient-on-my-network-indicate-an-attack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19726-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>"tsclient" recently appeared on a Windows 8 machine we have on our network. Reading around, it sounds like this is typically used for remote desktop applications. However, I haven't used any remote desktop services. (Unless some indirect application uses them? xbox glass?)</p><p>Could the appearance of tsclient indicate some sort of attack on my network? If so, what steps should I take to investigate?</p><p>Thank you for any help.</p></div><div id="question-tags" class="tags-container tags">tsclient attack investigate</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Mar '13, 11:49</strong></p><img src="https://secure.gravatar.com/avatar/8b67cd0522ada5463dd534bc69e3d515?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wheaton4prez&#39;s gravatar image" /><p>wheaton4prez<br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wheaton4prez has no accepted answers">0%</span></p></div></div><div id="comments-container-19726" class="comments-container"></div><div id="comment-tools-19726" class="comment-tools"></div><div class="clear"></div><div id="comment-19726-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19735"></span>

<div id="answer-container-19735" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19735-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>You need to be clear what you mean by "appeared". When you use RDP (remote desktop or Windows terminal services) to connect to another machine (for support reasons or to run an application), your local machine is seen by the remote machine as "\\tsclient". This allows you mount say a local drive or local printer as if it was connected to the machine. So on the remote machine "\\tclient\c$" would map to your local machines "C:\"</p><p>If you are allowing TCP port 3389 (the default port) in from other networks (for instance the Internet) and your machines are running the Remote Desktop service or Terminal Server service (not sure the exact name) then potential others can connect to your machine.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '13, 18:13</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p>martyvis<br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-19735" class="comments-container"><span id="19736"></span><div id="comment-19736" class="comment"><div id="post-19736-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your response. I should have clarified where tsclient appeared.</p><p>It was in the list of "Computer"s in the Network page of Windows Explorer. I did a reboot and it re-appeared in the same list along with computers that I know of on the network.</p></div><div id="comment-19736-info" class="comment-info"><span class="comment-age">(21 Mar '13, 18:32)</span> wheaton4prez</div></div><span id="19737"></span><div id="comment-19737" class="comment"><div id="post-19737-score" class="comment-score"></div><div class="comment-text"><p>Then, I systematically went around the house powering down all of our machines to see if one of them was causing it. Eventually, I had the machine completely isolated. Wireless was turned off. Modem disconnected from router. All LAN machines unplugged from router. But, it still listed tsclient as a computer on the network. After I rebooted with everything disconnected, it was gone. I reconnected all devices as before and it hasn't returned.</p></div><div id="comment-19737-info" class="comment-info"><span class="comment-age">(21 Mar '13, 18:32)</span> wheaton4prez</div></div><span id="19738"></span><div id="comment-19738" class="comment"><div id="post-19738-score" class="comment-score"></div><div class="comment-text"><p>These symptoms concern me because it seems consistent with someone gaining a remote connection somehow and then deciding to disconnect while I was troubleshooting.</p><p>I have not knowingly allowed port 3389 (or any other port for that matter). I have never run Remote Desktop or Terminal Services with this machine. Though, it's possible that they are on by default? (Windows 8)</p></div><div id="comment-19738-info" class="comment-info"><span class="comment-age">(21 Mar '13, 18:32)</span> wheaton4prez</div></div><span id="19739"></span><div id="comment-19739" class="comment"><div id="post-19739-score" class="comment-score"></div><div class="comment-text"><p>I don't have Win 8, but on Win7you can see the Remote Settings under My Computer:Properties. It shouldn't be allowed by default.</p><p>If I allow remote desktop, and run below from CMD, I get :-</p><p>C:\Users\me&gt;netstat -an | find ":3389"</p><p>TCP 0.0.0.0:3389 0.0.0.0:0 LISTENING</p><p>TCP [::]:3389 [::]:0 LISTENING</p><p>If Remote Desktop is not allowed, I get no result (which means there are no listeners).</p><p>My understanding is the "\\tsclient" would only appear in your Network folder after someone has connected to your machine via remote desktop.</p></div><div id="comment-19739-info" class="comment-info"><span class="comment-age">(21 Mar '13, 19:23)</span> martyvis</div></div><span id="19740"></span><div id="comment-19740" class="comment"><div id="post-19740-score" class="comment-score"></div><div class="comment-text"><p>Thank you. This is very helpful.</p><p>I looked in Remote Settings. "Allow Remote Assistance connections to this computer" is indeed checked. I never selected that. So, it was either by default in Windows 8 or it was somehow switched on without me knowing.</p><p>There is a separate section for "Remote Desktop" and "Don't allow remote connections to this computer" is selected.</p><p>I ran the netstat command you list and I got nothing. So, it didn't appear to be listening.</p><p>Given that information, do you think it's likely/possible that an uninvited connection was made? Would they have access to anything?</p></div><div id="comment-19740-info" class="comment-info"><span class="comment-age">(21 Mar '13, 21:20)</span> wheaton4prez</div></div><span id="19741"></span><div id="comment-19741" class="comment not_top_scorer"><div id="post-19741-score" class="comment-score"></div><div class="comment-text"><p>From what I've read, a person has to be "invited" in order to start Remote Assistance. This raises several questions:</p><p>Would there be a log somewhere of the invite and connection?</p><p>If someone tried to connect through remote assistance but failed due to lack of invite, might it still show tsclient on the network?</p><p>If someone successfully remoted in to a different computer on the network, is it possible that they would show on this computer as tsclient?</p><p>Does anyone know if there is a documented way/malware/etc. for a hacker to invite themselves into a Remote Assistance session?</p><p>Thanks again!</p></div><div id="comment-19741-info" class="comment-info"><span class="comment-age">(21 Mar '13, 21:51)</span> wheaton4prez</div></div></div><div id="comment-tools-19735" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-19735-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

