+++
type = "question"
title = "Unable to parse RTPS2 attributes through MATE or through display filter"
description = '''I have a network of machines all participating in a publish/subscribe environment using NDDS. My goal is to generate a list of all Topics and associated Messages. In addition, that list will include the publishers and subscribers of said messages. NDDS, according to Wireshark parsing, equates to RTP...'''
date = "2012-02-15T14:36:00Z"
lastmod = "2012-02-15T14:36:00Z"
weight = 9045
keywords = [ "mate", "wireshark" ]
aliases = [ "/questions/9045" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to parse RTPS2 attributes through MATE or through display filter](/questions/9045/unable-to-parse-rtps2-attributes-through-mate-or-through-display-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9045-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a network of machines all participating in a publish/subscribe environment using NDDS. My goal is to generate a list of all Topics and associated Messages. In addition, that list will include the publishers and subscribers of said messages.</p><p>NDDS, according to Wireshark parsing, equates to RTPS2 packets, and Wireshark has no problem parsing out the packets into awe-inspiring hierarchies. As there is specific data I want, I'd like to shortcut this and display only specific attributes of said messages.</p><p>I've decided to try to use MATE to grab just the information I need. I found the display reference guide for <a href="http://www.wireshark.org/docs/dfref/r/rtps2.html">RTPS2</a> and created the PDU described below. Though I get no errors when Wireshark loads the MATE config file, very few rtps2 attributes are actually showing up. The attributes that are purely alphabetical (e.g. <code>a</code>, <code>b</code>, <code>c</code>, <code>aa</code>...<code>an</code>, etc.) do not show up. Those with full words do.</p><p>Is there some piece staring me in the face that I don't see?</p><pre><code>Pdu rtps2_pdu Proto rtps2 Transport ip {
    Extract source_address From ip.src;
    Extract a From rtps2.appId;
    Extract b From rtps2.counter;
    Extract domain From rtps2.domain_id;
    Extract c From rtps2.guidPrefix;
    Extract d From rtps2.hostId;
    Extract e From rtps2.param.contentFilterName;
    Extract f From rtps2.param.entityName;
    Extract g From rtps2.param.filterName;
    Extract h From rtps2.param.groupData;
    Extract i From rtps2.param.id;
    Extract j From rtps2.param.length;
    Extract k From rtps2.param.ntpTime;
    Extract l From rtps2.param.ntpTime.fraction;
    Extract m From rtps2.param.ntpTime.sec;
    Extract n From rtps2.param.relatedTopicName;
    Extract o From rtps2.param.statusInfo;
    Extract p From rtps2.param.strength;
    Extract q From rtps2.param.topicData;
    Extract r From rtps2.param.topicName;
    Extract s From rtps2.param.typeName;
    Extract t From rtps2.param.userData;
    Extract participantId From rtps2.participant_idx;
    Extract u From rtps2.serializedData;
    Extract v From rtps2.sm.entityId;
    Extract w From rtps2.sm.entityId.entityKey;
    Extract x From rtps2.sm.entityId.entityKind;
    Extract y From rtps2.sm.flags;
    Extract z From rtps2.sm.guidPrefix;
    Extract aa From rtps2.sm.guidPrefix.appId;
    Extract ab From rtps2.sm.guidPrefix.appId.appKind;
    Extract ac From rtps2.sm.guidPrefix.appId.instanceId;
    Extract ad From rtps2.sm.guidPrefix.counter;
    Extract ae From rtps2.sm.guidPrefix.hostId;
    Extract af From rtps2.sm.id;
    Extract ag From rtps2.sm.octetsToNextHeader;
    Extract ah From rtps2.sm.rdEntityId;
    Extract ai From rtps2.sm.rdEntityId.entityKey;
    Extract aj From rtps2.sm.rdEntityId.entityKind;
    Extract ak From rtps2.sm.seqNumber;
    Extract al From rtps2.sm.wrEntityId;
    Extract am From rtps2.sm.wrEntityId.entityKey;
    Extract an From rtps2.sm.wrEntityId.entityKind;
    Extract traffic_nature From rtps2.traffic_nature;
    Extract vendorId From rtps2.vendorId;
    Extract version From rtps2.version;
    Extract version_major From rtps2.version.major;
    Extract verson_minor From rtps2.version.minor;
};

Done;</code></pre></div><div id="question-tags" class="tags-container tags">mate wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Feb '12, 14:36</strong></p><img src="https://secure.gravatar.com/avatar/f693f5f46ba4ed6e7fa7fc82667a4dcf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pgcordell&#39;s gravatar image" /><p>pgcordell<br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pgcordell has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Feb '12, 08:34</p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-9045" class="comments-container"><span id="9065"></span><div id="comment-9065" class="comment"><div id="post-9065-score" class="comment-score"></div><div class="comment-text"><p>Do you mean that the "name" you give a Pdu affects whether you get the field extract or not? For example in this case:</p><p>Extract a From rtps2.appId;</p><p>"a" does not work because "a" is too short? In other words, it would/does work if you change "a" to "aaaaaa" or something longer?</p></div><div id="comment-9065-info" class="comment-info"><span class="comment-age">(16 Feb '12, 07:49)</span> JeffMorriss ♦</div></div><span id="9068"></span><div id="comment-9068" class="comment"><div id="post-9068-score" class="comment-score"></div><div class="comment-text"><p>No, I haven't seen any effect of changing the "name" portion of an Extract. I get the same result from the following lines:</p><p><code> Extract a From rtps2.appId; or Extract a1 From rtps2.appId; or Extract aa From rtps2.appId; or Extract myAppID From rtps2.appId;</code></p><p>One thing I'm wondering is if I need to define anything else? If I intentionally screw up references to an rtps2 field, I get an error. If I do it correctly, I get no error but I also get no data.</p><p>For example, according to the link, there exists a reference to "rtps2.param.topicName". If I use the following line:</p><p><code> Extract topicName From rtps2.param.topicName;</code></p><p>I get no error, but the myTopicName doesn't show up the PDU display either. If instead I intentionally use the wrong reference and leave out the "param":</p><p><code> Extract myTopicName From rtps2.topicName;</code></p><p>I get the following error:</p><p>"MATE Error: cannot find field for attribute myTopicName"</p><p>So... I know that the field exists and that I'm referring to it correctly. But I still get no data.</p></div><div id="comment-9068-info" class="comment-info"><span class="comment-age">(16 Feb '12, 09:16)</span> pgcordell</div></div><span id="9075"></span><div id="comment-9075" class="comment"><div id="post-9075-score" class="comment-score"></div><div class="comment-text"><p>Stupid question: are you sure the frames you're looking at have the fields you're looking for? E.g., if you filter for "rtps2.appId" you get the frame? What happens if you add the filter item as a "custom column"? Does the value you're looking for show up there?</p><p>If the fields are really there then I'd suggest opening a bug with a sample script and capture file.</p></div><div id="comment-9075-info" class="comment-info"><span class="comment-age">(16 Feb '12, 13:38)</span> JeffMorriss ♦</div></div><span id="50166"></span><div id="comment-50166" class="comment"><div id="post-50166-score" class="comment-score"></div><div class="comment-text"><p>I'm going to guess that it's the same bug affecting <a href="https://ask.wireshark.org/questions/48499/using-mate-with-mgcp">mgcp</a>.</p></div><div id="comment-50166-info" class="comment-info"><span class="comment-age">(12 Feb '16, 14:36)</span> cmaynard ♦♦</div></div><span id="50530"></span><div id="comment-50530" class="comment"><div id="post-50530-score" class="comment-score"></div><div class="comment-text"><p>The bug affecting mgcp seems to me as if related to the mgcp <em>dissector</em>, because MATE debug says, in case of mgcp, that the mgcp part of the packet ranges from octet 42 to octet 42.</p><p>I'll open a bug on that in a while, but I first wanted to check whether these two issues could really be related. However, extraction of another field (<code>rtsp.vendorId</code>) from rtsp went smoothly, and I don't have any capture where any packet would contain the <code>rtsp.param.topicName</code> field.</p><p>@pgcordell, do you happen to still have one four years after?</p></div><div id="comment-50530-info" class="comment-info"><span class="comment-age">(26 Feb '16, 03:52)</span> sindy</div></div></div><div id="comment-tools-9045" class="comment-tools"></div><div class="clear"></div><div id="comment-9045-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

