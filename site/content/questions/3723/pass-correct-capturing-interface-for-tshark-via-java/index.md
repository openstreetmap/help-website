+++
type = "question"
title = "pass correct capturing interface for tshark via JAVA"
description = '''Hi all, At this moment, I am trying to implement a &quot;one-click&quot; packet capturing functionality (button on a GUI) in one of my JAVA applications, with the help of tshark/wireshark. So far, I tried this:  String nic = NetworkInterface.getName(); String execute = &quot;C:&#92;Progra~1&#92;Wireshark&#92;tshark -i &quot;+nic+&quot;...'''
date = "2011-04-26T10:56:00Z"
lastmod = "2011-04-26T10:56:00Z"
weight = 3723
keywords = [ "nic", "java", "tshark", "networkinterface" ]
aliases = [ "/questions/3723" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [pass correct capturing interface for tshark via JAVA](/questions/3723/pass-correct-capturing-interface-for-tshark-via-java)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3723-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>At this moment, I am trying to implement a "one-click" packet capturing functionality (button on a GUI) in one of my JAVA applications, with the help of tshark/wireshark.</p><p>So far, I tried this:</p><hr /><p>String nic = NetworkInterface.getName();</p><p>String execute = "C:\Progra~1\Wireshark\tshark -i "+nic+" -b filesize:512 -w testCap";</p><p>try { Runtime.getRuntime().exec(execute); }</p><p>catch (IOException e1) { msg("Error during initialization of live capture"); e1.printStackTrace(); }</p><hr /><p>It turns out that String nic contains the name of the (via the GUI) selected local NIC, like for example "eth0."</p><p>I am using tshark on a pc running Windows7, and this type of NIC name that is returned by the method NetworkInterface.getName() is not recognized by tshark, since I receive the following message;</p><p>"tshark: The capture session could not be initiated (Error opening adapter: the system cannot find the device. (20)) Please check that "eth0" is the proper interface"</p><p>Any suggestions? Thanks a lot in advance!</p></div><div id="question-tags" class="tags-container tags">nic java tshark networkinterface</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Apr '11, 10:56</strong></p><img src="https://secure.gravatar.com/avatar/5deb4519306a8bcc3ee954cbb479cc00?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="robbertottenhof&#39;s gravatar image" /><p>robbertottenhof<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="robbertottenhof has no accepted answers">0%</span></p></div></div><div id="comments-container-3723" class="comments-container"></div><div id="comment-tools-3723" class="comment-tools"></div><div class="clear"></div><div id="comment-3723-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

