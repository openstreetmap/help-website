+++
type = "question"
title = "Numerical values of SNMP parameters as text"
description = '''Hi! I connected the device mib module and has a file with the description of the SNMP parameters for this device. What can be done to the numerical values ​​of the SNMP parameters to be displayed in Wireshark as text. Thnx.'''
date = "2017-01-21T13:26:00Z"
lastmod = "2017-01-22T03:44:00Z"
weight = 58935
keywords = [ "snmp_text_values" ]
aliases = [ "/questions/58935" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Numerical values of SNMP parameters as text](/questions/58935/numerical-values-of-snmp-parameters-as-text)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58935-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi! I connected the device mib module and has a file with the description of the SNMP parameters for this device. What can be done to the numerical values ​​of the SNMP parameters to be displayed in Wireshark as text. Thnx.</p></div><div id="question-tags" class="tags-container tags">snmp_text_values</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jan '17, 13:26</strong></p><img src="https://secure.gravatar.com/avatar/9d4f2ecdca8bfd16374ac5736582af80?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Magister&#39;s gravatar image" /><p>Magister<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Magister has no accepted answers">0%</span></p></div></div><div id="comments-container-58935" class="comments-container"></div><div id="comment-tools-58935" class="comment-tools"></div><div class="clear"></div><div id="comment-58935-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58942"></span>

<div id="answer-container-58942" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58942-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>All relevant preferences are found in Preferences | Namre Resolution, in the SMI related options. Once set, restart Wireshark (unfortunately there's no runtime reconfiguration) and test the results. Be aware of error reports when the MIBs are loaded, libsmi is rather critical about correctness of the MIB.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '17, 03:44</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-58942" class="comments-container"><span id="58955"></span><div id="comment-58955" class="comment"><div id="post-58955-score" class="comment-score"></div><div class="comment-text"><p>Hi! Unfortunately, you do not understand me. There are satellite modem Comtech CDM-570L. There is a mib module for it (CDM-570L-MIB), which I plugged in Wireshark. Now, Wireshark displays the name of the modem parameters and their numerical values ​​(for example, modulation: 0, etc.). The modem has a guide table with a text description of numeric values ​​(for example, modulation: 0 - qpsk, 1 - 8psk etc.). That's the question, how to get Wireshark display text instead of numeric values ​​(for example, modulation: 8psk)? Uhhh... Thnx.</p></div><div id="comment-58955-info" class="comment-info"><span class="comment-age">(22 Jan '17, 13:16)</span> Magister</div></div><span id="58956"></span><div id="comment-58956" class="comment"><div id="post-58956-score" class="comment-score"></div><div class="comment-text"><p>I moved your note to a comment. Are the encodings in the user guide part of the mib? Wireshark would not know about tables that are part of user guides only.</p></div><div id="comment-58956-info" class="comment-info"><span class="comment-age">(22 Jan '17, 13:28)</span> Bob Jones</div></div><span id="58957"></span><div id="comment-58957" class="comment"><div id="post-58957-score" class="comment-score">1</div><div class="comment-text"><p>@Magister: For that you'll have to augment the relevant object(s) in the MIB. All I could find was a CDM-570-MIB with object cdm570HigherOrderModulation, which does have named values for its syntax. So it seems that you'll need to load that MIB too, before CDM-570L-MIB.</p></div><div id="comment-58957-info" class="comment-info"><span class="comment-age">(22 Jan '17, 14:39)</span> Jaap ♦</div></div><span id="59001"></span><div id="comment-59001" class="comment"><div id="post-59001-score" class="comment-score"></div><div class="comment-text"><p>Jaap, thanks! I understand your idea (edit the mib file) and I will try.</p></div><div id="comment-59001-info" class="comment-info"><span class="comment-age">(24 Jan '17, 01:31)</span> Magister</div></div><span id="59010"></span><div id="comment-59010" class="comment"><div id="post-59010-score" class="comment-score"></div><div class="comment-text"><p>@Magister: If you load CDM-570-MIB as well as CDM-570L-MIB you likely won't even have to.</p></div><div id="comment-59010-info" class="comment-info"><span class="comment-age">(24 Jan '17, 05:53)</span> Jaap ♦</div></div></div><div id="comment-tools-58942" class="comment-tools"></div><div class="clear"></div><div id="comment-58942-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

