+++
type = "question"
title = "Create a rule set from scratch based on wireshark capture"
description = '''Hello I&#x27;m a new registered user to this site, but have already been using it from time to time when strange questions occured in the past :) So first, thank you for all the help already provided :) I have been asked a strange question: some users are moving, and my management wonders why we couldn&#x27;t...'''
date = "2013-09-06T01:14:00Z"
lastmod = "2013-09-09T08:16:00Z"
weight = 24410
keywords = [ "ruleset", "wireshark" ]
aliases = [ "/questions/24410" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Create a rule set from scratch based on wireshark capture](/questions/24410/create-a-rule-set-from-scratch-based-on-wireshark-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24410-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24410-score" class="post-score" title="current number of votes">0</div><span id="post-24410-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello I'm a new registered user to this site, but have already been using it from time to time when strange questions occured in the past :) So first, thank you for all the help already provided :)</p><p>I have been asked a strange question: some users are moving, and my management wonders why we couldn't capture network traffic on some user's computer during a day, and use all the data collected to produce a rule set that'll be pushed on the new firewall to come. Despite the fact that monitoring one user's network activity isn't really a good way to get all traffic, has someone ever done that? and do you know tools that could be of any help in this attempt?</p><p>Thank you very much!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ruleset" rel="tag" title="see questions tagged &#39;ruleset&#39;">ruleset</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Sep '13, 01:14</strong></p><img src="https://secure.gravatar.com/avatar/c034368638ad6252b0341f3732e77d3c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="go3th&#39;s gravatar image" /><p><span>go3th</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="go3th has no accepted answers">0%</span></p></div></div><div id="comments-container-24410" class="comments-container"></div><div id="comment-tools-24410" class="comment-tools"></div><div class="clear"></div><div id="comment-24410-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24414"></span>

<div id="answer-container-24414" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24414-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24414-score" class="post-score" title="current number of votes">0</div><span id="post-24414-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>some users are moving, and <strong>my management wonders</strong> why we couldn't <strong>capture network traffic on some user's computer</strong> during a day, <strong>and use all the data</strong> collected <strong>to produce a rule set</strong> that'll be pushed on the new firewall to come.</p></blockquote><p>well, that does not sound like a very good idea. A firewall shall only allow what is absolutely necessary (<a href="http://en.wikipedia.org/wiki/Principle_of_least_privilege">principle of least privilege</a>). If you capture the traffic of a single system and use the systems network activity as a base for the firewall rule set, security will go down the drain and honestly then you don't need a firewall at all. A router would be much cheaper ;-))</p><p>So, my answer to your question is three-fold.</p><ol><li>It is technically possible to create firewall rule sets from a pcap and I have done that in very certain and limited scenarios. See below.</li><li>It would be much easier to use the current firewall logs and/or the current firewall rule set to create a policy for the new firewall, as that obviously reflects what the user is allowed to do through the current firewall and <strong>hopefully</strong> also reflects your security policy.</li><li>From a security point of view it is not clever to use the traffic of a system as the base for a firewall rule set. Just remind you management on this: What happens if the user is not trustworthy. With the intended way to configure the new firewall, you could open a hole for that user to leak internal information (documents, price calculations, payroll info, etc.). The firewall would then be totally useless and should be replaced by a much cheaper router.</li></ol><p>So, if you still want to use the capture file, here is how you could do it.</p><ul><li>You need a very good understanding of the new firewall architecture <strong>and</strong> figure out how you can automatically create a rule set (including the network objects) for the new firewall. That works good for some products as they either offer a CLI or a text based configuration (Check Point, Juniper, Fortigate, iptables). For some products it may not work at all, because the configuration uses a proprietary format (binary, 'encrypted', etc.) and/or does not provide a CLI.</li><li>Then use tshark to list all conversations of that user (after you have captured the data):</li></ul><blockquote><p>tshark -nr input.pcap -q -z conv,udp<br />
tshark -nr input.pcap -q -z conv,tcp</p></blockquote><ul><li>Take the output of tshark and create a meta policy (internal representation of the firewall rule set) with a script (perl, python, whatever).</li><li>Convert the meta poliy into something that your new firewall product understands and push it to the new firewall</li></ul><p>I'm not aware of any product that will do it automatically for you. There may be open source projects, but I don't know one either.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Sep '13, 02:05</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Sep '13, 02:12</strong> </span></p></div></div><div id="comments-container-24414" class="comments-container"><span id="24418"></span><div id="comment-24418" class="comment"><div id="post-24418-score" class="comment-score"></div><div class="comment-text"><p>Well, thank you very much. I just joined my new compagny, and that's one of the first thing they asked me to check. I was a bit suscipicious, but now, I won't hesitate to tell them that's it's a bad idea.</p><p>Thank you again!</p></div><div id="comment-24418-info" class="comment-info"><span class="comment-age">(06 Sep '13, 04:42)</span> <span class="comment-user userinfo">go3th</span></div></div><span id="24482"></span><div id="comment-24482" class="comment"><div id="post-24482-score" class="comment-score"></div><div class="comment-text"><p>good luck.</p></div><div id="comment-24482-info" class="comment-info"><span class="comment-age">(09 Sep '13, 08:16)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-24414" class="comment-tools"></div><div class="clear"></div><div id="comment-24414-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

