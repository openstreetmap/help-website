+++
type = "question"
title = "Is there a way to edit a pcap file to remove addresses?"
description = '''I have a saved pcap file that needs to be edited to remove address. Then save the file back as pcap so the Wireshark features can be used.  I’m exporting the file. Export -&amp;gt; Export Packet Dissection -&amp;gt; as Plain Text file. Make the changes. Now I need to import the file and save as pcap. Is thi...'''
date = "2013-02-28T18:45:00Z"
lastmod = "2016-04-13T17:52:00Z"
weight = 18998
keywords = [ "import", "export" ]
aliases = [ "/questions/18998" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Is there a way to edit a pcap file to remove addresses?](/questions/18998/is-there-a-way-to-edit-a-pcap-file-to-remove-addresses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18998-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18998-score" class="post-score" title="current number of votes">0</div><span id="post-18998-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a saved pcap file that needs to be edited to remove address. Then save the file back as pcap so the Wireshark features can be used.<br />
</p><p>I’m exporting the file. Export -&gt; Export Packet Dissection -&gt; as Plain Text file. Make the changes. Now I need to import the file and save as pcap.</p><p>Is this possible?</p><p>Any help is worth a beer or two!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Feb '13, 18:45</strong></p><img src="https://secure.gravatar.com/avatar/51c851f70d3b7083a7b05d95a34a66b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="VoIP%20This&#39;s gravatar image" /><p><span>VoIP This</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="VoIP This has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Mar '13, 10:53</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-18998" class="comments-container"></div><div id="comment-tools-18998" class="comment-tools"></div><div class="clear"></div><div id="comment-18998-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="19014"></span>

<div id="answer-container-19014" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19014-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19014-score" class="post-score" title="current number of votes">4</div><span id="post-19014-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="VoIP This has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If ultimate purpose is just editing the pcap file, I would suggest using a pcap editing tool like <a href="http://bittwist.sourceforge.net/">bittwist</a>, <a href="https://code.google.com/p/libcrafter/">libcrafter</a>,<a href="http://www.wireshark.org/docs/man-pages/editcap.html">editcap</a>,<a href="http://tcpreplay.synfin.net/wiki/tcprewrite">tcprewrite</a>,<a href="http://netdude.sourceforge.net/">netdude</a> or <a href="http://sourceforge.net/projects/powereditpcap/">powereditpcap</a>. It would be way easier to use these tools than exporting as txt, editing it and exporting back as pcap.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Feb '13, 23:04</strong></p><img src="https://secure.gravatar.com/avatar/46196bc495ce51058590c4e4ae334d22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SidR&#39;s gravatar image" /><p><span>SidR</span><br />
<span class="score" title="245 reputation points">245</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SidR has 3 accepted answers">30%</span></p></div></div><div id="comments-container-19014" class="comments-container"><span id="19520"></span><div id="comment-19520" class="comment"><div id="post-19520-score" class="comment-score"></div><div class="comment-text"><p>Thanks SidR. I'll have to read up on the above tools in order to edit out the public addresses and replace them with pseudo addresses. Once again thanks SidR.</p></div><div id="comment-19520-info" class="comment-info"><span class="comment-age">(14 Mar '13, 13:07)</span> <span class="comment-user userinfo">VoIP This</span></div></div><span id="51654"></span><div id="comment-51654" class="comment"><div id="post-51654-score" class="comment-score"></div><div class="comment-text"><p>editcap won't work for this purpose - it doesn't understand packet payloads - but at least some of the other tools should be able to do that.</p></div><div id="comment-51654-info" class="comment-info"><span class="comment-age">(13 Apr '16, 17:52)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-19014" class="comment-tools"></div><div class="clear"></div><div id="comment-19014-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19567"></span>

<div id="answer-container-19567" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19567-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19567-score" class="post-score" title="current number of votes">1</div><span id="post-19567-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Some resources on anonymizing network traces:</p><ul><li><a href="http://sharkfest.wireshark.org/sharkfest.11/presentations/A-11_Bongertz-Trace_File_Anonymization.pdf">a Sharkfest presentation on trace file anonymization</a>, which mentions some tools;</li><li><a href="http://ask.wireshark.org/questions/844/utility-to-anonymize-capture-files">an answer to another ask.wireshark.org question on this topic</a>;</li><li><a href="http://comments.gmane.org/gmane.network.tcpdump.devel/5106">an e-mail message I sent on the tcpdump-workers mailing list answering somebody's question about anonymization</a>;</li><li><a href="http://www.cc.gatech.edu/computing/Networking/projects/cryptopan/">an anonymizing tool mentioned in the FAQ for the CAIDA data sets</a>;</li><li><a href="http://www.tm.uka.de/software/pktanon/">another anonymizing tool</a> mentioned in <a href="http://taosecurity.blogspot.com/2008/07/packet-anonymization-with-pktanon.html">a blog post</a> about it;</li><li><a href="http://scrub-tcpdump.sourceforge.net/index.php">still another tool</a> that showed up in <a href="https://www.google.com/search?client=safari&amp;rls=en&amp;q=anonymizing+pcap+files&amp;ie=UTF-8&amp;oe=UTF-8">the Google search</a> I used to find these resources;</li><li><a href="http://netexpect.org/wiki">and another packet manipulating tool</a> whose Wiki gives <a href="http://netexpect.org/wiki/RewriteAndReplay">an example of how to anonymize IPv4 addresses with it</a>;</li><li><a href="http://crawdad.cs.dartmouth.edu/meta.php?name=tools/sanitize/generic/AnonTool">and another tool</a> linked to by the site for the CRAWDAD data sets.</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Mar '13, 11:11</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-19567" class="comments-container"></div><div id="comment-tools-19567" class="comment-tools"></div><div class="clear"></div><div id="comment-19567-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="51652"></span>

<div id="answer-container-51652" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51652-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51652-score" class="post-score" title="current number of votes">0</div><span id="post-51652-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Another library you can use it <a href="http://seladb.github.io/PcapPlusPlus-Doc/">PcapPlusPlus</a> (<a href="https://github.com/seladb/PcapPlusPlus">github</a> repo). It has all sorts of parsing and editing capabilities, among them is editing IP addresses</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Apr '16, 14:17</strong></p><img src="https://secure.gravatar.com/avatar/0b6fc0687623a56d9f42c88153062754?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="seladb&#39;s gravatar image" /><p><span>seladb</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="seladb has no accepted answers">0%</span></p></div></div><div id="comments-container-51652" class="comments-container"></div><div id="comment-tools-51652" class="comment-tools"></div><div class="clear"></div><div id="comment-51652-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

