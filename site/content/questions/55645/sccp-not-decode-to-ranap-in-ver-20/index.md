+++
type = "question"
title = "SCCP not decode to RANAP in Ver 2.0+"
description = '''I tested V2 and V2.2 for my pcap file. but both version can not decode one SCCP message (same issue on other pcap file for Attach_rej or Auth_Rej DTAP messages) but V1.10 or V.12 can decode it. I can&#x27;t share my pcap file. please tell me how to fix it. I have Attached both image:   '''
date = "2016-09-19T04:57:00Z"
lastmod = "2016-09-19T08:57:00Z"
weight = 55645
keywords = [ "decode", "sccp", "wireshark-2.0", "ranap" ]
aliases = [ "/questions/55645" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SCCP not decode to RANAP in Ver 2.0+](/questions/55645/sccp-not-decode-to-ranap-in-ver-20)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55645-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55645-score" class="post-score" title="current number of votes">0</div><span id="post-55645-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I tested V2 and V2.2 for my pcap file. but both version can not decode one SCCP message (same issue on other pcap file for Attach_rej or Auth_Rej DTAP messages) but V1.10 or V.12 can decode it. I can't share my pcap file. please tell me how to fix it. I have Attached both image:</p><h2 id="v1.10"><img src="http://e80.imgup.net/2a6c9.PNG" alt="V1.10" /></h2><hr /><p><img src="http://r55.imgup.net/1160a.PNG" alt="V2.00" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decode" rel="tag" title="see questions tagged &#39;decode&#39;">decode</span> <span class="post-tag tag-link-sccp" rel="tag" title="see questions tagged &#39;sccp&#39;">sccp</span> <span class="post-tag tag-link-wireshark-2.0" rel="tag" title="see questions tagged &#39;wireshark-2.0&#39;">wireshark-2.0</span> <span class="post-tag tag-link-ranap" rel="tag" title="see questions tagged &#39;ranap&#39;">ranap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Sep '16, 04:57</strong></p><img src="https://secure.gravatar.com/avatar/1875074c024268a57d8f261ff216b36f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dehban&#39;s gravatar image" /><p><span>Dehban</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dehban has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Sep '16, 04:58</strong> </span></p></div></div><div id="comments-container-55645" class="comments-container"><span id="55646"></span><div id="comment-55646" class="comment"><div id="post-55646-score" class="comment-score"></div><div class="comment-text"><p>I Think there is a bug in recent versions (after 2.0)</p><p>How to verify the bug?</p></div><div id="comment-55646-info" class="comment-info"><span class="comment-age">(19 Sep '16, 05:09)</span> <span class="comment-user userinfo">Dehban</span></div></div><span id="55648"></span><div id="comment-55648" class="comment"><div id="post-55648-score" class="comment-score">1</div><div class="comment-text"><p>Can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>?</p></div><div id="comment-55648-info" class="comment-info"><span class="comment-age">(19 Sep '16, 05:34)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="55656"></span><div id="comment-55656" class="comment"><div id="post-55656-score" class="comment-score">1</div><div class="comment-text"><p>In general, if privacy concerns prevent you from publishing the problematic capture, the choices are the following:</p><ul><li><p>save only the problematic frame to a separate file and publish that single-frame file (which may not address all privacy issues and may not illustrate the issue enough if the frame needs some context so that the issue occurs. In your particular case you have the tools to check that the behaviour is the same on a single frame).</p></li><li><p>[file a bug][1] and mark the attached capture file as a private one, which will make it accessible only to the core developers.</p></li><li><p>use a tool with anonymization capabilities like Tracewrangler before publishing the file (in your case, this is not a choice as I guess the identifiers you want to keep secret are not only in the IP layer)</p></li><li><p>export the frame in question as a hex dump, anonymize it manually, re-import it back to check that the addresses have changed while Wireshark's handling has not, and publish the resulting capture file.</p></li></ul></div><div id="comment-55656-info" class="comment-info"><span class="comment-age">(19 Sep '16, 06:57)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="55657"></span><div id="comment-55657" class="comment"><div id="post-55657-score" class="comment-score"></div><div class="comment-text"><p>Temporal file Link [48 Hours]: <a href="http://expirebox.com/download/d080c29b99d33370802f0d6bd01a68a4.html">Link</a></p></div><div id="comment-55657-info" class="comment-info"><span class="comment-age">(19 Sep '16, 07:02)</span> <span class="comment-user userinfo">Dehban</span></div></div><span id="55658"></span><div id="comment-55658" class="comment"><div id="post-55658-score" class="comment-score"></div><div class="comment-text"><p>4th message has been attached. 2nd and 3rd chunk could not be decoded by ver2+</p></div><div id="comment-55658-info" class="comment-info"><span class="comment-age">(19 Sep '16, 07:11)</span> <span class="comment-user userinfo">Dehban</span></div></div><span id="55660"></span><div id="comment-55660" class="comment not_top_scorer"><div id="post-55660-score" class="comment-score"></div><div class="comment-text"><p>Please note if you have same issue on Ver2+ [windows]</p></div><div id="comment-55660-info" class="comment-info"><span class="comment-age">(19 Sep '16, 07:57)</span> <span class="comment-user userinfo">Dehban</span></div></div><span id="55662"></span><div id="comment-55662" class="comment not_top_scorer"><div id="post-55662-score" class="comment-score"></div><div class="comment-text"><p>I do, but given the Answer of <span>@JeffMorris</span>, it's not a surprise.</p></div><div id="comment-55662-info" class="comment-info"><span class="comment-age">(19 Sep '16, 08:10)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="55664"></span><div id="comment-55664" class="comment not_top_scorer"><div id="post-55664-score" class="comment-score"></div><div class="comment-text"><p>well... maybe there are actually two issues?</p><p>First, there is a workaround of the bug <span>@JeffMorris</span> refers to. With 2.2.0, you can use <code>File -&gt; Export PDUs to File</code> and choose <code>OSI Layer 3</code> as export type. This will create a new capture file and open it instead of the original one. In the new file, each MTP3 and above part of the original frames gets its own frame (with a special encapsulation but that shouldn't bother you much).</p><p>The second point is whether the decoding of the first RANAP message is correct or not. In your screenshots, the summary description of the first message in the dissection pane differs, while in packet list it is the same (id-Iu-Release). Do you disagree with how the messages are dissected after exporting them as described above?</p></div><div id="comment-55664-info" class="comment-info"><span class="comment-age">(19 Sep '16, 08:57)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-55645" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-55645-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55661"></span>

<div id="answer-container-55661" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55661-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55661-score" class="post-score" title="current number of votes">1</div><span id="post-55661-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like you're running into <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11130">bug 11130</a>. The workaround is to disable SCCP reassembly (that will cause all the PDUs to be dissected as RANAP).</p><p>You might want to add yourself to the Cc: list of that bug to track its progress.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Sep '16, 08:04</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></img></div></div><div id="comments-container-55661" class="comments-container"></div><div id="comment-tools-55661" class="comment-tools"></div><div class="clear"></div><div id="comment-55661-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

