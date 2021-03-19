+++
type = "question"
title = "Fragmentation problems"
description = '''I&#x27;m facing several problems on handling fragmented packets. Actually I have a packet with a 0x8F length, that comes in 2 parts, the first one with 0x72, the second with the rest of the packet with some extra bytes (The total size as well the fragment size can change , but I think my problem is not t...'''
date = "2012-01-23T07:15:00Z"
lastmod = "2012-01-23T07:15:00Z"
weight = 8562
keywords = [ "fragment", "fragmentation", "reassemble", "split" ]
aliases = [ "/questions/8562" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Fragmentation problems](/questions/8562/fragmentation-problems)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8562-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm facing several problems on handling fragmented packets. Actually I have a packet with a 0x8F length, that comes in 2 parts, the first one with 0x72, the second with the rest of the packet with some extra bytes (The total size as well the fragment size can change , but I think my problem is not that).</p><p>What I'm doing is:</p><pre><code>save_fragmented = pinfo-&gt;fragmented;
fragment_data *frag_msg = fragment_add_seq_check ( tvb, 1, pinfo, nRXCounter, //Key of the packet
iso7816_fragment_table, 
iso7816_reassembled_table,
nFrameCounter, // guint32 fragment sequence number starting with value 1
tvb_length(tvb),
FALSE);
if (frag_msg) /* Reassembled */
{ 
 col_append_str(pinfo-&gt;cinfo, COL_INFO,&quot; R E A S S E M B L E D &quot;);
}
else /* Not last packet of reassembled Message */
{
 col_append_fstr(pinfo-&gt;cinfo, COL_INFO,&quot; (Message fragment # %u)&quot;, nFrameCounter++);
}</code></pre><p>I thought that by passing the last argument as FALSE it would stop the fragmentation and set the frag_items with the tvb data for the two incoming packets, but it doesn't happen. Instead of give me the frag_msg with some data to be reassembled, it consider that the packet is still being fragmented and the Wireshark shows "Message fragment #1"",2,3" and so on...</p><p>My doubst are: Is the 8th argument the length of the REMAINING size of the total 8F? Or is the size of the fragment being passed to the function at that time? e.g: Since the total size is 8F, in the first fragment(that has a 0x72 length) i should pass the 0x72 value or a 0x8F-0x72 value? The last argument, should be false or true to STOP the fragmentation and answer with the fragmented data until that moment?? The developers guide is not so clear at this point, so I will be grateful if anyone can help me.</p><p>Regards,</p><p>Francesco</p></div><div id="question-tags" class="tags-container tags">fragment fragmentation reassemble split</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jan '12, 07:15</strong></p><img src="https://secure.gravatar.com/avatar/95ae97a9326bb3f819dca9d383e58cf6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tchesko&#39;s gravatar image" /><p>Tchesko<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tchesko has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Jan '12, 07:18</p></div></div><div id="comments-container-8562" class="comments-container"></div><div id="comment-tools-8562" class="comment-tools"></div><div class="clear"></div><div id="comment-8562-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

