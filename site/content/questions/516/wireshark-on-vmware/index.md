+++
type = "question"
title = "Wireshark On VMware"
description = '''We are building a multi server SIPX cluster and wish to be able to build a monitoring platform with six NICs. The optimal configuration would be to run six virtual machines with an instance of Wireshare running on each VM. Has any one out there done this? Does Wireshark run on UNIX and if so what ve...'''
date = "2010-10-15T07:47:00Z"
lastmod = "2010-10-19T16:08:00Z"
weight = 516
keywords = [ "linux-support", "mutiple-nics" ]
aliases = [ "/questions/516" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark On VMware](/questions/516/wireshark-on-vmware)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-516-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We are building a multi server SIPX cluster and wish to be able to build a monitoring platform with six NICs. The optimal configuration would be to run six virtual machines with an instance of Wireshare running on each VM.</p><p>Has any one out there done this? Does Wireshark run on UNIX and if so what versions...CentOS? How much much RAM is required? Will it work with a QUAD core single CPU box or does it require multiple physical CPUs?</p><p>Thank You,</p></div><div id="question-tags" class="tags-container tags">linux-support mutiple-nics</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Oct '10, 07:47</strong></p><img src="https://secure.gravatar.com/avatar/97ccb343a49c720cc908bc55e029ad41?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrbodle&#39;s gravatar image" /><p>mrbodle<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrbodle has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Oct '10, 16:11</p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span></p></div></div><div id="comments-container-516" class="comments-container"></div><div id="comment-tools-516" class="comment-tools"></div><div class="clear"></div><div id="comment-516-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="546"></span>

<div id="answer-container-546" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-546-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>First of all, yes, Wireshark runs on most platforms but getting it to capture data might involve some work since it needs capture access to the NIC. It usually doesn't matter if the OS is running on bare metal or in a VM - if there is a Wireshark flavour for it, it will work in a VM.</p><p>Regarding doing captures in VMware you need to be aware that there are different virtualization plattforms like VMWare Server, VMWare Workstation and VMWare vSphere. While VMWare Server and Workstation are quite similar in their network setups the ESX server of vSphere are configured differently and use virtual switches which the other two do not.</p><p>I guess that you want to use the free VMware Server 2.x. In that case you can create six VMs and install the OS of your choice and then Wireshark in each of them (dumpcap or tcpdump might be enough if you just want to capture and not analyze inside the VM). Then you need to map the virtual NIC of each VM to a separate physical NIC in bridge mode. If I remember correctly (I do mostly vSphere now) this has to be done using the vmnetcfg utility that can be found in the VMWare server install directory.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Oct '10, 16:08</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-546" class="comments-container"></div><div id="comment-tools-546" class="comment-tools"></div><div class="clear"></div><div id="comment-546-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="517"></span>

<div id="answer-container-517" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-517-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Could you read the <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChapterIntroduction.html">Introduction</a> section of the User's Guide and see what questions remain?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Oct '10, 07:54</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-517" class="comments-container"></div><div id="comment-tools-517" class="comment-tools"></div><div class="clear"></div><div id="comment-517-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

