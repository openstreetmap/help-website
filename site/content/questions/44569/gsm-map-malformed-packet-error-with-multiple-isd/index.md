+++
type = "question"
title = "gsm-map - malformed packet error with multiple ISD"
description = '''Hi, I am working with implementing a new IE that is included in the Insert Subscriber Data message (from the HLR to the SGSN). The attribute is called &quot;APN-OI-Replacement&quot; and is a a part of the GPRSSubscriptionData sequence. I am pasting the ASN.1 below: (from 29.002) GPRSSubscriptionData ::= SEQUE...'''
date = "2015-07-28T09:52:00Z"
lastmod = "2015-07-28T09:52:00Z"
weight = 44569
keywords = [ "gsm_map" ]
aliases = [ "/questions/44569" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [gsm-map - malformed packet error with multiple ISD](/questions/44569/gsm-map-malformed-packet-error-with-multiple-isd)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44569-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am working with implementing a new IE that is included in the Insert Subscriber Data message (from the HLR to the SGSN). The attribute is called "APN-OI-Replacement" and is a a part of the GPRSSubscriptionData sequence. I am pasting the ASN.1 below: (from 29.002)</p><p>GPRSSubscriptionData ::= SEQUENCE { completeDataListIncluded NULL OPTIONAL, -- If segmentation is used, completeDataListIncluded may only be present in the -- first segment of GPRSSubscriptionData. gprsDataList [1] GPRSDataList, extensionContainer [2] ExtensionContainer OPTIONAL, ..., apn-oi-Replacement [3] APN-OI-Replacement OPTIONAL -- this apn-oi-Replacement refers to the UE level apn-oi-Replacement. }</p><p>Now the issue I have is this. Since the the gprsDataList attribute is not marked as optional, it MUST be present in the ISD for it to be properly decoded. In the case of a multiple ISD (when the ISD is split up into multiple chunks) and in the particular case where the ISD is split up such that the gprsDataList goes in the first ISD, while the apn-oi-Replacement is in the second ISD, then the second ISD appears as malformed in wireshark. (because wireshark thinks we are sending the APN-OI-Replacement without the mandatory gprsDataList).</p><p>My question to the readers here is this: - Is this really a problem in the real network? Would an SGSN understand that the second ISD was part of a sequence and accept it as such? - Do you think there is any solution to this? The breakup into multiple ISD's might occur at different boundaries depending on the TCAP and other settings. Any suggestions?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">gsm_map</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jul '15, 09:52</strong></p><img src="https://secure.gravatar.com/avatar/1f993507f4676e4154cbeca51a354bec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Abelli&#39;s gravatar image" /><p>Abelli<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Abelli has no accepted answers">0%</span></p></div></div><div id="comments-container-44569" class="comments-container"><span id="44579"></span><div id="comment-44579" class="comment"><div id="post-44579-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure I understand, shouldn't that be one is message split in several tcap or sctp chunks?</p></div><div id="comment-44579-info" class="comment-info"><span class="comment-age">(28 Jul '15, 13:50)</span> Anders ♦</div></div><span id="44620"></span><div id="comment-44620" class="comment"><div id="post-44620-score" class="comment-score"></div><div class="comment-text"><p>Sorry I used the wrong term. It is several tcap messages. Not SCTP chunks.</p></div><div id="comment-44620-info" class="comment-info"><span class="comment-age">(29 Jul '15, 23:12)</span> Abelli</div></div></div><div id="comment-tools-44569" class="comment-tools"></div><div class="clear"></div><div id="comment-44569-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

