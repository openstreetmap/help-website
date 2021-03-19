+++
type = "question"
title = "Opening an exported file"
description = '''Last night I was running some pcaps and wanted to analyze them at school today, so being a noob at wireshark and not seeing an obvious save option in the File menu i went down to export and selected C arrays since i guessed that that would be importable and would be the most specific save. Now today...'''
date = "2010-11-30T05:51:00Z"
lastmod = "2010-11-30T07:13:00Z"
weight = 1176
keywords = [ "import", "c", "export", "array" ]
aliases = [ "/questions/1176" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Opening an exported file](/questions/1176/opening-an-exported-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1176-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1176-score" class="post-score" title="current number of votes">0</div><span id="post-1176-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Last night I was running some pcaps and wanted to analyze them at school today, so being a noob at wireshark and not seeing an obvious save option in the File menu i went down to export and selected C arrays since i guessed that that would be importable and would be the most specific save. Now today I'm looking around and I don't see any way to import it into wireshark, I did look at text2pcap but as far as I can tell it doesn't convert C arrays to pcaps. All help is appreciated!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-c" rel="tag" title="see questions tagged &#39;c&#39;">c</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-array" rel="tag" title="see questions tagged &#39;array&#39;">array</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Nov '10, 05:51</strong></p><img src="https://secure.gravatar.com/avatar/42ed3397512f4a3404d5dee6af46cb80?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="monks700&#39;s gravatar image" /><p><span>monks700</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="monks700 has no accepted answers">0%</span></p></div></div><div id="comments-container-1176" class="comments-container"></div><div id="comment-tools-1176" class="comment-tools"></div><div class="clear"></div><div id="comment-1176-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1180"></span>

<div id="answer-container-1180" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1180-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1180-score" class="post-score" title="current number of votes">1</div><span id="post-1180-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is <code>"File -&gt; Save"</code> in the menu, it's even above the Export option. That is the way to save packets for later analysis.</p><p>I gues if you <em>really</em> need the data from the C-arrays, you can write a C program that writes the packet data back to a libpcap based file. However, the c-arrays only contain the RAW packet data without the libpcap header (so no timestamps), you'd have to fabricate the libpcap headers (file header and packets headers) yourself.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Nov '10, 07:13</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-1180" class="comments-container"></div><div id="comment-tools-1180" class="comment-tools"></div><div class="clear"></div><div id="comment-1180-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

