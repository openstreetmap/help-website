+++
type = "question"
title = "SNMP and Destination IP Address"
description = '''Hello All, Just starting out using Wireshark and I have all kinds of SNMP traffic from a inside source going to several destination IP addresses in the private subnet range that are not IP&#x27;s that I use in my network. Why would these addresses show? Thanks in advance.'''
date = "2013-04-08T07:01:00Z"
lastmod = "2013-04-08T14:56:00Z"
weight = 20174
keywords = [ "snmpwireshark" ]
aliases = [ "/questions/20174" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [SNMP and Destination IP Address](/questions/20174/snmp-and-destination-ip-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20174-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20174-score" class="post-score" title="current number of votes">0</div><span id="post-20174-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello All,</p><p>Just starting out using Wireshark and I have all kinds of SNMP traffic from a inside source going to several destination IP addresses in the private subnet range that are not IP's that I use in my network. Why would these addresses show?</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-snmpwireshark" rel="tag" title="see questions tagged &#39;snmpwireshark&#39;">snmpwireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Apr '13, 07:01</strong></p><img src="https://secure.gravatar.com/avatar/69004980b6fc9e83b0b23810f04e30b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mccullrr&#39;s gravatar image" /><p><span>mccullrr</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mccullrr has no accepted answers">0%</span></p></div></div><div id="comments-container-20174" class="comments-container"></div><div id="comment-tools-20174" class="comment-tools"></div><div class="clear"></div><div id="comment-20174-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20176"></span>

<div id="answer-container-20176" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20176-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20176-score" class="post-score" title="current number of votes">2</div><span id="post-20176-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You should determine the source IP to see what kind of device it is. I have seen a couple of cases where laptops had printer drivers installed where the actual printer wasn't reachable but SNMP packets are still trying to get to them. This happens e.g. when a user installs a printer at home and brings the laptop to the company network. The laptop will try to contact the home printer (to check toner status and what not), and of course it will not receive an answer, but you'll still see the queries.</p><p>Another way to find out what happens is to google for the SNMP code that is queried, e.g. "1.3.7...". Often, you can find what kind of device is supposed to be contacted.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Apr '13, 07:06</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-20176" class="comments-container"></div><div id="comment-tools-20176" class="comment-tools"></div><div class="clear"></div><div id="comment-20176-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20178"></span>

<div id="answer-container-20178" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20178-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20178-score" class="post-score" title="current number of votes">1</div><span id="post-20178-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A lot of server management software (Dell Server Manager, HP, etc.) or printer management software (HP, Samsung) or any other network management tool tries to monitor components with SNMP. Sometimes those systems come with pre-configured IP addresses.</p><p>I suggest to look at the SNMP requests and then search the OID (Wireshark will tell you) via google. That should reveal some further information. If you can't find anything (or don't understand the SNMP protocol) you can post the capture file somewhere (google docs, dropbox, cloudshark.org - BEWARE privacy issues!).</p><p>BTW: What do you know about the system that sends the SNMP requests? Is that a server (possibly with nagios or similar) or a client machine?<br />
</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Apr '13, 07:18</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Apr '13, 07:27</strong> </span></p></div></div><div id="comments-container-20178" class="comments-container"><span id="20187"></span><div id="comment-20187" class="comment"><div id="post-20187-score" class="comment-score"></div><div class="comment-text"><p>Thanks guys. This is a web / file server and the info is showing get-request 1.3.6.1.2.1.1.2.0. Ah, you know what. It is running a software package called FMAudit that looks out and pulls data from printers on the network. Maybe that is causing this?</p></div><div id="comment-20187-info" class="comment-info"><span class="comment-age">(08 Apr '13, 08:58)</span> <span class="comment-user userinfo">mccullrr</span></div></div><span id="20192"></span><div id="comment-20192" class="comment"><div id="post-20192-score" class="comment-score"></div><div class="comment-text"><p>There's a few ways to test that... if FMAudit isn't critical then try to shut it down for some time to see if the SNMP packets disappear. If it is critical or you have someone who can tell you faster than looking at a trace, analyze it's configuration to see if the target IPs you noticed are configured as objects that are queried.</p></div><div id="comment-20192-info" class="comment-info"><span class="comment-age">(08 Apr '13, 11:43)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="20206"></span><div id="comment-20206" class="comment"><div id="post-20206-score" class="comment-score"></div><div class="comment-text"><p>OID <a href="http://tools.cisco.com/Support/SNMP/do/BrowseOID.do?local=en&amp;translate=Translate&amp;objectInput=1.3.6.1.2.1.1.2">1.3.6.1.2.1.1.2.0</a> is the sysObjectID. So, that piece of software is probably trying to identify the type of the devices (printer) on a pre-configured subnet.</p><p>As <span></span><span>@Jasper</span> said. Disable the FMAudit software and see what happens.</p></div><div id="comment-20206-info" class="comment-info"><span class="comment-age">(08 Apr '13, 14:56)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-20178" class="comment-tools"></div><div class="clear"></div><div id="comment-20178-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

