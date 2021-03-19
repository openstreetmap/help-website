+++
type = "question"
title = "NT Status: STATUS_UNSUCCESSFUL (0xc0000001)"
description = '''trying to save a scanned file from a Canon copier running MEAP (Multifunctional Embedded Application Platform) to an SMB share on NetApp 2240 (C-Mode) generates a meaningless error on the copier. Wireshark capture from the scanner side shows a successful 3 way handshake, then SMB protocol negotiatio...'''
date = "2013-09-05T10:55:00Z"
lastmod = "2013-09-05T11:54:00Z"
weight = 24386
keywords = [ "canon", "netapp", "smb" ]
aliases = [ "/questions/24386" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [NT Status: STATUS\_UNSUCCESSFUL (0xc0000001)](/questions/24386/nt-status-status_unsuccessful-0xc0000001)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24386-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>trying to save a scanned file from a Canon copier running MEAP (Multifunctional Embedded Application Platform) to an SMB share on NetApp 2240 (C-Mode) generates a meaningless error on the copier.</p><p>Wireshark capture from the scanner side shows a successful 3 way handshake, then SMB protocol negotiation request which gets an error response from NetApp "NT Status: STATUS_UNSUCCESSFUL (0xc0000001)"</p><p>What would be an indication that the SMB request from the copier is non-Unicode ?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">canon netapp smb</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Sep '13, 10:55</strong></p><img src="https://secure.gravatar.com/avatar/bcfdf26904f3a8a9fb69c7ca0dc5e7b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="net_tech&#39;s gravatar image" /><p>net_tech<br />
<span class="score" title="116 reputation points">116</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="net_tech has 2 accepted answers">13%</span></p></div></div><div id="comments-container-24386" class="comments-container"></div><div id="comment-tools-24386" class="comment-tools"></div><div class="clear"></div><div id="comment-24386-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24390"></span>

<div id="answer-container-24390" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24390-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>What would be an indication that the SMB request from the copier is non-Unicode ?</p></blockquote><p>That depends on what you mean by "non-Unicode".</p><p>I'm looking at one SMB trace that I have; the Negotiate Protocol request has the "Strings are Unicode" flag set in the Flags2 field, but the protocol names are non-Unicode, as Microsoft's MS-CIFS specification says they should be:</p><blockquote><p>String fields that restrict character encoding to OEM characters only, even if Unicode support has been negotiated, are labeled as OEM_STRING. Some examples of strings that are never passed in Unicode are:</p><ul><li>The dialect strings in the SMB_COM_NEGOTIATE (section 2.2.4.52) command.</li></ul></blockquote></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Sep '13, 11:54</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-24390" class="comments-container"><span id="24393"></span><div id="comment-24393" class="comment"><div id="post-24393-score" class="comment-score"></div><div class="comment-text"><p>In the SMB request packet, under Flags2 I see Unicode Strings: Strings are ASCII</p><p>I am running in to a BUG described in the article below.</p><p><a href="http://support.netapp.com/NOW/cgi-bin/bol?Type=Detail&amp;Display=617674">http://support.netapp.com/NOW/cgi-bin/bol?Type=Detail&amp;Display=617674</a></p><p>The CIFS-enabled Vserver disallows any SMB 1 requests that do not have the Unicode bit set. This happens even if there are not any Unicode strings sent in the request.</p></div><div id="comment-24393-info" class="comment-info"><span class="comment-age">(05 Sep '13, 12:08)</span> net_tech</div></div></div><div id="comment-tools-24390" class="comment-tools"></div><div class="clear"></div><div id="comment-24390-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

