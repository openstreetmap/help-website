+++
type = "question"
title = "How do I identify every IP address on my local network?"
description = '''Hello,  I live in a flat with 5 other people and I want to find out the IP address for each computer in my flat, in each room there is a telephone port to connect each computer to the internet via a Ethernet cable, pleas help. many thanks Andy'''
date = "2011-12-09T08:55:00Z"
lastmod = "2013-06-21T04:00:00Z"
weight = 7876
keywords = [ "ip", "lan", "dhcp" ]
aliases = [ "/questions/7876" ]
osqa_answers = 5
osqa_accepted = false
+++

<div class="headNormal">

# [How do I identify every IP address on my local network?](/questions/7876/how-do-i-identify-every-ip-address-on-my-local-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7876-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7876-score" class="post-score" title="current number of votes">0</div><span id="post-7876-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I live in a flat with 5 other people and I want to find out the IP address for each computer in my flat, in each room there is a telephone port to connect each computer to the internet via a Ethernet cable, pleas help.</p><p>many thanks Andy</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-lan" rel="tag" title="see questions tagged &#39;lan&#39;">lan</span> <span class="post-tag tag-link-dhcp" rel="tag" title="see questions tagged &#39;dhcp&#39;">dhcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Dec '11, 08:55</strong></p><img src="https://secure.gravatar.com/avatar/5c82658590630d1d5fc9725368a41c9f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andypickleton456&#39;s gravatar image" /><p><span>andypickleto...</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andypickleton456 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Dec '11, 09:20</strong> </span></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-7876" class="comments-container"></div><div id="comment-tools-7876" class="comment-tools"></div><div class="clear"></div><div id="comment-7876-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

5 Answers:

</div>

</div>

<span id="7877"></span>

<div id="answer-container-7877" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7877-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7877-score" class="post-score" title="current number of votes">0</div><span id="post-7877-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>While capable of performing this task, Wireshark is probably overkill and not the best or easiest way to do so. Home networks usually come together at one point, and that is usually a router that performs DHCP to assign addresses to every device on the network. Just log in to your router and look at the DHCP table for a neat summary of IP Addresses to MAC Addresses (and probably Computer Names as well).</p><p>I assume by "telephone port" you mean "ethernet jack", and that your flat has network cables run in some way that make them difficult to follow (in the walls, under the floors, etc). Wherever your modem is plugged in to the phone or cable jack to go to the Internet is probably where your router is as well. If you must use Wireshark for this task, you will probably need to do some slight modification to your network setup as described in the <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet#Switched_Ethernet" title="Switched Ethernet">Switched Ethernet</a> wiki article.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Dec '11, 09:19</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-7877" class="comments-container"><span id="7878"></span><div id="comment-7878" class="comment"><div id="post-7878-score" class="comment-score"></div><div class="comment-text"><p>Thank You, but the network in my flat is controlled from a outside source I am in halls it is owned and operated by the university, so I am not sure how that would work but I will give it a try</p></div><div id="comment-7878-info" class="comment-info"><span class="comment-age">(09 Dec '11, 09:23)</span> <span class="comment-user userinfo">andypickleto...</span></div></div><span id="7879"></span><div id="comment-7879" class="comment"><div id="post-7879-score" class="comment-score"></div><div class="comment-text"><p>In that case, things will probably be more difficult. Can't you ask them what their IP addresses are? The University is probably switched, and you will specifically <strong>not</strong> be able to do anything about it. If your friends run Windows, ask them to run <code>ipconfig</code> at a command prompt and tell you the IP address. If they run linux, as them to run <code>ifconfig</code> at the command line and tell you the IP address.</p></div><div id="comment-7879-info" class="comment-info"><span class="comment-age">(09 Dec '11, 09:31)</span> <span class="comment-user userinfo">multipleinte...</span></div></div><span id="7881"></span><div id="comment-7881" class="comment"><div id="post-7881-score" class="comment-score"></div><div class="comment-text"><p>I'm trying to do it on the sly, plus they mostly have mac's</p></div><div id="comment-7881-info" class="comment-info"><span class="comment-age">(09 Dec '11, 10:10)</span> <span class="comment-user userinfo">andypickleto...</span></div></div></div><div id="comment-tools-7877" class="comment-tools"></div><div class="clear"></div><div id="comment-7877-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7892"></span>

<div id="answer-container-7892" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7892-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7892-score" class="post-score" title="current number of votes">0</div><span id="post-7892-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try NMAP - it's free and a very common tool amongst Wireshark users. Look at your own ipconfig for the LAN address and then do a scan based on the IP/subnet you see there. No promises because the university's network may regard the scan as a prelude to a cyber attack but most do not.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Dec '11, 23:21</strong></p><img src="https://secure.gravatar.com/avatar/f797bdc41d990dca073837114e048b1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EricKnaus&#39;s gravatar image" /><p><span>EricKnaus</span><br />
<span class="score" title="46 reputation points">46</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EricKnaus has no accepted answers">0%</span></p></div></div><div id="comments-container-7892" class="comments-container"></div><div id="comment-tools-7892" class="comment-tools"></div><div class="clear"></div><div id="comment-7892-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7901"></span>

<div id="answer-container-7901" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7901-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7901-score" class="post-score" title="current number of votes">0</div><span id="post-7901-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>nmap is the way to go. If you know the size of your network, do a nmap scan with</p><p>nmap -sP 192.168.0.0/24</p><p>This of course is a simple class C. But that should let you know of others that are on your network.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Dec '11, 14:04</strong></p><img src="https://secure.gravatar.com/avatar/a132ed8bc0ebce606397080f40341738?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NetSamSpade&#39;s gravatar image" /><p><span>NetSamSpade</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NetSamSpade has no accepted answers">0%</span></p></div></div><div id="comments-container-7901" class="comments-container"></div><div id="comment-tools-7901" class="comment-tools"></div><div class="clear"></div><div id="comment-7901-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7980"></span>

<div id="answer-container-7980" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7980-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7980-score" class="post-score" title="current number of votes">0</div><span id="post-7980-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>With the suggested nmap scan, you will probably find a lot more IP addresses than just those of the 5 nodes in your flat. The network has its own topology and does not care about walls, flats, locations (apart from latencies). With the nmap against a class C subnet in a University it is likely you harvest several 10s, probably more then 100 or even 200 IP addresses (depends on how many are up and running at scan time). The University might regard that as an infringement of their policies. I'd rather not run that scan but ask my friends (I do not have a MAC but OS X is UNIX based, maybe it has also an ifconfig executable ...). However, if the addresses are not static but DHCP-provided and hence dynamic, those addresses are likely to change with every reboot (or network reset or ...).</p><p>Uwe</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '11, 12:21</strong></p><img src="https://secure.gravatar.com/avatar/79f833616dc05e5e83e524c8513ad2e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ufalke&#39;s gravatar image" /><p><span>ufalke</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ufalke has no accepted answers">0%</span></p></div></div><div id="comments-container-7980" class="comments-container"></div><div id="comment-tools-7980" class="comment-tools"></div><div class="clear"></div><div id="comment-7980-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22219"></span>

<div id="answer-container-22219" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22219-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22219-score" class="post-score" title="current number of votes">0</div><span id="post-22219-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can open the <a href="http://www.ip-details.com/">IP-Details.com</a> to find the Internet IP address in every PC.</p><p>To find the computer IP address: For windows OS: Start---&gt;run--&gt;Type cmd Then command prompt will display. type ipconfig</p><p>For Linux OS: Goto terminal---&gt;type ifconfig .</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '13, 04:00</strong></p><img src="https://secure.gravatar.com/avatar/22a525d6b0891ccc4842d61db33d2407?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="VelaiyatuPillai&#39;s gravatar image" /><p><span>VelaiyatuPillai</span><br />
<span class="score" title="10 reputation points">10</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="VelaiyatuPillai has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Jun '13, 04:03</strong> </span></p></div></div><div id="comments-container-22219" class="comments-container"></div><div id="comment-tools-22219" class="comment-tools"></div><div class="clear"></div><div id="comment-22219-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

