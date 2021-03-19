+++
type = "question"
title = "Wireshark not reading vendor diameter xml."
description = '''Hi I am using Version 1.12.6 (v1.12.6-0-gee1fce6 from master-1.12) in 32 bit windows. I am decoding a diameter trace. In my dictionary file, I have (just mentioning relevant parts):   ...other entitities ]&amp;gt;  &amp;lt;vendor vendor-id=&quot;Ericsson&quot; code=&quot;193&quot; name=&quot;Ericsson&quot;/&amp;gt;  &amp;amp;Ericsson;  Then in ...'''
date = "2015-06-26T03:52:00Z"
lastmod = "2015-06-26T03:52:00Z"
weight = 43584
keywords = [ "diameter", "dictionary" ]
aliases = [ "/questions/43584" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark not reading vendor diameter xml.](/questions/43584/wireshark-not-reading-vendor-diameter-xml)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43584-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I am using Version 1.12.6 (v1.12.6-0-gee1fce6 from master-1.12) in 32 bit windows. I am decoding a diameter trace.</p><p>In my dictionary file, I have (just mentioning relevant parts):</p>...other entitities ]&gt;<pre><code>&lt;vendor vendor-id=&quot;Ericsson&quot;  code=&quot;193&quot; name=&quot;Ericsson&quot;/&gt;

&amp;Ericsson;</code></pre><p>Then in the same folder I have Ericsson.xml. It seems when I decode it is not reading anything outside of dictionary.xml. For example:</p><p>When I add this in dictionary.xml it is read and decoded:</p><pre><code>&lt;avp name=&quot;Service-Provider-Id&quot; code=&quot;1081&quot; mandatory=&quot;must&quot; vendor-bit=&quot;must&quot; vendor-id=&quot;Ericsson&quot; may-encrypt=&quot;no&quot; protected=&quot;mustnot&quot;&gt;
  &lt;type type-name=&quot;UTF8String&quot;/&gt;
&lt;/avp&gt;</code></pre><p>But when I have this AVP definition is in Ericsson.xml, wireshark doesnt decode it. it says "if you know this add this in dictionary.xml"</p><p>Just wondering what else I can do.</p><p>regards H</p></div><div id="question-tags" class="tags-container tags">diameter dictionary</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jun '15, 03:52</strong></p><img src="https://secure.gravatar.com/avatar/0b8fc1d1b3e98c058442c7fa0d480302?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HASAN&#39;s gravatar image" /><p>HASAN<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HASAN has no accepted answers">0%</span></p></div></div><div id="comments-container-43584" class="comments-container"><span id="43599"></span><div id="comment-43599" class="comment"><div id="post-43599-score" class="comment-score"></div><div class="comment-text"><p>Do you have your own version of Ericsson.xml or,adding to the existing one? There may have been changes in the format.</p></div><div id="comment-43599-info" class="comment-info"><span class="comment-age">(27 Jun '15, 07:42)</span> Anders ♦</div></div></div><div id="comment-tools-43584" class="comment-tools"></div><div class="clear"></div><div id="comment-43584-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

