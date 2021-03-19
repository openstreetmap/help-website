+++
type = "question"
title = "List of protocol in the PCAP file"
description = '''Hi there, I am looking to analyse a PCAP file generated using wireshark. Is there any possibility to use a filter that generates a list of protocols found in the capture? same thing with the list IPs and host/domain names in the capture file. Regards'''
date = "2016-08-18T07:54:00Z"
lastmod = "2016-08-18T14:59:00Z"
weight = 54951
keywords = [ "pcap", "wireshark" ]
aliases = [ "/questions/54951" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [List of protocol in the PCAP file](/questions/54951/list-of-protocol-in-the-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54951-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54951-score" class="post-score" title="current number of votes">0</div><span id="post-54951-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there, I am looking to analyse a PCAP file generated using wireshark. Is there any possibility to use a filter that generates a list of protocols found in the capture? same thing with the list IPs and host/domain names in the capture file.</p><p>Regards</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Aug '16, 07:54</strong></p><img src="https://secure.gravatar.com/avatar/4baa23bf58c8fa559cdbb0e3331c7e63?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="geniusgenie007&#39;s gravatar image" /><p><span>geniusgenie007</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="geniusgenie007 has no accepted answers">0%</span></p></div></div><div id="comments-container-54951" class="comments-container"></div><div id="comment-tools-54951" class="comment-tools"></div><div class="clear"></div><div id="comment-54951-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="54952"></span>

<div id="answer-container-54952" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54952-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54952-score" class="post-score" title="current number of votes">1</div><span id="post-54952-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have a look at the Wireshark Statistics menu, in particular the Protocol Hierarchy and Endpoints options.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Aug '16, 08:10</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-54952" class="comments-container"><span id="54953"></span><div id="comment-54953" class="comment"><div id="post-54953-score" class="comment-score"></div><div class="comment-text"><p>Actually, I am looking to use custom filters to do this task to make myself understand wireshark better.</p></div><div id="comment-54953-info" class="comment-info"><span class="comment-age">(18 Aug '16, 08:12)</span> <span class="comment-user userinfo">geniusgenie007</span></div></div><span id="54954"></span><div id="comment-54954" class="comment"><div id="post-54954-score" class="comment-score"></div><div class="comment-text"><p>This can't be done with filters, as they only give a match\no match for each frame to display it and don't take into account values in other frames. To show distinct values among frames, e.g. protocol hierarchy requires a "tap" which is what the items under the statistics menu use.</p></div><div id="comment-54954-info" class="comment-info"><span class="comment-age">(18 Aug '16, 08:26)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-54952" class="comment-tools"></div><div class="clear"></div><div id="comment-54952-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="54956"></span>

<div id="answer-container-54956" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54956-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54956-score" class="post-score" title="current number of votes">1</div><span id="post-54956-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You'll probably want to do that kind of think in tshark (as Graham said, this isn't something to do with filters).</p><p>For your specific example of getting all the protocols in a file there's actually already a shell script for that (in the Wireshark source code, it's not installed when you install Wireshark): <code>tools/list_protos_in_cap.sh</code>.</p><p>Fundamentally the script just runs <code>tshark -T fields -e frame.protocols -nr /path/to/file</code> then does a little more magic to remove duplicate protocols.</p><p>Similar mechanisms can be used to find IP addresses, etc.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Aug '16, 10:27</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-54956" class="comments-container"><span id="54963"></span><div id="comment-54963" class="comment"><div id="post-54963-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot Jeff and Graham, I will definitely give it a try.</p></div><div id="comment-54963-info" class="comment-info"><span class="comment-age">(18 Aug '16, 14:59)</span> <span class="comment-user userinfo">geniusgenie007</span></div></div></div><div id="comment-tools-54956" class="comment-tools"></div><div class="clear"></div><div id="comment-54956-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

