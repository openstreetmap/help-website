+++
type = "question"
title = "Custom wireshark dissector plugin: unable to overwrite col_protocol and info"
description = '''Hello, I have written a custom dissector plugin for internal use and am using &quot;WTAP_ENCAP_USER0&quot; as port. In my dissector, I am setting protocol name and info field using col_set_str function. But it still shows the entry set in packet-frame.c. The protocol field is displayed as UNKNOWN and info fie...'''
date = "2017-02-01T13:51:00Z"
lastmod = "2017-02-01T13:51:00Z"
weight = 59232
keywords = [ "dissector", "plugin" ]
aliases = [ "/questions/59232" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Custom wireshark dissector plugin: unable to overwrite col\_protocol and info](/questions/59232/custom-wireshark-dissector-plugin-unable-to-overwrite-col_protocol-and-info)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59232-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have written a custom dissector plugin for internal use and am using "WTAP_ENCAP_USER0" as port. In my dissector, I am setting protocol name and info field using col_set_str function.</p><p>But it still shows the entry set in packet-frame.c. The protocol field is displayed as UNKNOWN and info field as WTAP_ENCAP = 45. If I comment out this line in packet-frame.c, then I can see the information and protocol that I set.</p><p>How can make my col_set_str to take effect and display my protocol and info instead</p></div><div id="question-tags" class="tags-container tags">dissector plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Feb '17, 13:51</strong></p><img src="https://secure.gravatar.com/avatar/dd9838ab086fed6c7c24a109d07abe8f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rashmi_s&#39;s gravatar image" /><p>rashmi_s<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rashmi_s has no accepted answers">0%</span></p></div></div><div id="comments-container-59232" class="comments-container"><span id="59233"></span><div id="comment-59233" class="comment"><div id="post-59233-score" class="comment-score"></div><div class="comment-text"><p>To add, I have already configured edit-&gt;preferences-&gt;DLT_USERS and also see that my protocol is enable in analyze-&gt;enabled protocols</p></div><div id="comment-59233-info" class="comment-info"><span class="comment-age">(01 Feb '17, 14:35)</span> rashmi_s</div></div></div><div id="comment-tools-59232" class="comment-tools"></div><div class="clear"></div><div id="comment-59232-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

