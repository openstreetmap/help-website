+++
type = "question"
title = "Promiscuous Mode NIC Adapter Setup Required?"
description = '''Do I need to enable my NIC for Promiscuous Mode under Windows, or does Wireshark do this automatically? Pursuant to my last question, I&#x27;m trying to intercept traffic between two remote machines via a HUB connection. Also, I can&#x27;t find any instructions for how to do this under Windows 10. I found a l...'''
date = "2017-10-19T11:16:00Z"
lastmod = "2017-10-21T04:54:00Z"
weight = 64033
keywords = [ "promiscuous-mode" ]
aliases = [ "/questions/64033" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Promiscuous Mode NIC Adapter Setup Required?](/questions/64033/promiscuous-mode-nic-adapter-setup-required)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-64033-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-64033-score" class="post-score" title="current number of votes">0</div><span id="post-64033-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Do I need to enable my NIC for Promiscuous Mode under Windows, or does Wireshark do this automatically? Pursuant to my last question, I'm trying to intercept traffic between two remote machines via a HUB connection.</p><p>Also, I can't find any instructions for how to do this under Windows 10. I found a link for Windows 7 instructions, but they don't seem to work on Windows 10.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-promiscuous-mode" rel="tag" title="see questions tagged &#39;promiscuous-mode&#39;">promiscuous-mode</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Oct '17, 11:16</strong></p><img src="https://secure.gravatar.com/avatar/84e4e0eca8f98b778f0b41fec5db25f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dcs&#39;s gravatar image" /><p><span>dcs</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dcs has no accepted answers">0%</span></p></div></div><div id="comments-container-64033" class="comments-container"></div><div id="comment-tools-64033" class="comment-tools"></div><div class="clear"></div><div id="comment-64033-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="64036"></span>

<div id="answer-container-64036" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-64036-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-64036-score" class="post-score" title="current number of votes">0</div><span id="post-64036-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Click on Edit &gt; Preferences &gt; Capture and you'll see the preference "Capture packets in promiscuous mode". As long as that is checked, which is Wireshark's default, Wireshark will put the adapter into promiscuous mode for you when you start capturing. If the adapter was not already in promiscuous mode, then Wireshark will switch it back when you stop capturing.</p><p>So yes, Wireshark does this automatically, as long as you haven't disabled this preference.</p><p>This should be the same, regardless of whether Wireshark is installed on Windows 7 or Windows 10.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Oct '17, 13:24</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-64036" class="comments-container"><span id="64037"></span><div id="comment-64037" class="comment"><div id="post-64037-score" class="comment-score"></div><div class="comment-text"><p>Glad to hear that. So I don't understand why I can't see traffic on the HUB that isn't directly communicating with the Wireshark computer. Please see my previous question about intercepting packets between two remote computers.</p><p>I could use a telephone consultant!</p></div><div id="comment-64037-info" class="comment-info"><span class="comment-age">(19 Oct '17, 15:16)</span> <span class="comment-user userinfo">dcs</span></div></div><span id="64038"></span><div id="comment-64038" class="comment"><div id="post-64038-score" class="comment-score"></div><div class="comment-text"><p>I changed your "answer" to a comment. That's how this site works.</p><p>As Jasper said in his answer to your other question, just because it's labeled as a hub, doesn't mean it is. It's very likely to be a switch. Back when hubs were still commonly used, it was cheaper for the manufacturers to use one chip set for both hubs and switches. Of course, the switch had to have switching capability. So they labeled one device as a switch and the other as a hub, and sold the hub for a lower price, but they were actually both switches.</p><p>Jaap pointed out that you can do remote capture through an SSH tunnel. Or you could simply capture directly on the Redhat box with tcpdump and then copy your capture file to your Windows PC and load it into Wireshark for analysis. Even if you are going to use Wireshark for analysis, it doesn't have to be your capture program.</p></div><div id="comment-64038-info" class="comment-info"><span class="comment-age">(19 Oct '17, 16:26)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div></div><div id="comment-tools-64036" class="comment-tools"></div><div class="clear"></div><div id="comment-64036-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="64063"></span>

<div id="answer-container-64063" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-64063-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-64063-score" class="post-score" title="current number of votes">0</div><span id="post-64063-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As you wrote that your hub is a real one, not a switch bearing a label "hub", it is a correct way of thinking that the issue may be related to the capturing machine and that promiscuous mode might be switched off.</p><p>Now even if Wireshark (via WinPcap) successfully switches the network interface to promiscuous mode, there may be an anti-virus/firewall filter hooked to that interface and drop packets which do not match local MAC and/or IP address even though the packet filter does let them through, and this filter may be "closer to the wire" than WinPcap's own capturing "filter".</p><p>So go to network adapter settings and check whether, in the list of protocols and other items, you cannot disable a filter bearing the name of your anti-virus or firewall software. If there is no such item, it still does not mean that the firewall or antivirus does not do this; if there is, disabling it before starting to capture may solve your issue. In such case, it may help to disable the functionality in the firewall/antivirus control panel.</p><p>Another possibility could be to set up a software bridge consisting of two network cards and capture at one of the members while the antivirus/firewall should interfere with the virtual interface connected to the bridge. But this requires that you have a second network card as otherwise Windows won't allow you to create the bridge. On the other hand, you may use a USB network card, create the bridge, and then disconnect the USB card - the bridge will survive.</p><p>Yet another possibility is to replace WinPcap with <a href="https://nmap.org/npcap/">npcap</a> which hooks to a different place in the network stack, so you may be lucky and this place may be closer to the wire than the one where the antivirus hooks in.</p><p>The last resort would be to uninstall your antivirus/firewall before capturing (which usually includes a reboot of the machine because the filters often remain in place until reboot).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '17, 04:54</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-64063" class="comments-container"></div><div id="comment-tools-64063" class="comment-tools"></div><div class="clear"></div><div id="comment-64063-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

