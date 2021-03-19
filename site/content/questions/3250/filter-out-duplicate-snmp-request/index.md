+++
type = "question"
title = "Filter out duplicate SNMP Request"
description = '''Hi, I&#x27;m using Wireshark to solve a SNMP problem. I have some large pcap-files full of SNMP traffic. Some SNMP Requests have the same SNMP Request-ID. Is it possible to filter out duplicate SNMP Request IDs with a display filter or is there a solution with tshark? Thanks for your help!'''
date = "2011-03-31T11:54:00Z"
lastmod = "2011-03-31T13:11:00Z"
weight = 3250
keywords = [ "filter", "request", "duplicate", "snmp", "id" ]
aliases = [ "/questions/3250" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Filter out duplicate SNMP Request](/questions/3250/filter-out-duplicate-snmp-request)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3250-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3250-score" class="post-score" title="current number of votes">0</div><span id="post-3250-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm using Wireshark to solve a SNMP problem. I have some large pcap-files full of SNMP traffic. Some SNMP Requests have the same SNMP Request-ID. Is it possible to filter out duplicate SNMP Request IDs with a display filter or is there a solution with tshark?</p><p>Thanks for your help!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span> <span class="post-tag tag-link-duplicate" rel="tag" title="see questions tagged &#39;duplicate&#39;">duplicate</span> <span class="post-tag tag-link-snmp" rel="tag" title="see questions tagged &#39;snmp&#39;">snmp</span> <span class="post-tag tag-link-id" rel="tag" title="see questions tagged &#39;id&#39;">id</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Mar '11, 11:54</strong></p><img src="https://secure.gravatar.com/avatar/945a2ebc37274af06332de5c7daef9db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DrJekyll&#39;s gravatar image" /><p><span>DrJekyll</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DrJekyll has no accepted answers">0%</span></p></div></div><div id="comments-container-3250" class="comments-container"></div><div id="comment-tools-3250" class="comment-tools"></div><div class="clear"></div><div id="comment-3250-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3255"></span>

<div id="answer-container-3255" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3255-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3255-score" class="post-score" title="current number of votes">1</div><span id="post-3255-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="DrJekyll has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hey, did someone say 'tshark'? :-)</p><p>Yes, you can achieve what you want with tshark and some command line tools (I can't think of a way to do it within Wireshark):</p><pre><code>$ tshark -r tmp.cap -R snmp -T fields -e snmp.request_id 
1614590690
1614590690
1614590690
1614590690
$</code></pre><p>As you can see, my tmp.cap file does indeed have a duplicate request-id. You can now get a list of all duplicate request-id's by piping the output through 'sort' and 'uniq -d':</p><pre><code>$ tshark -r tmp.cap -R snmp -T fields -e snmp.request_id | sort | uniq -d
1614590690
$</code></pre><p>(uniq -d just lists duplicate entries, see 'man uniq')</p><p>If you are running tshark on Windows, you can install <a href="http://www.cygwin.com">Cygwin</a> to get a (bash) shell and command line tools.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Mar '11, 13:03</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-3255" class="comments-container"><span id="3258"></span><div id="comment-3258" class="comment"><div id="post-3258-score" class="comment-score"></div><div class="comment-text"><p>Thanks SYNbit. This looks great. I will try it out! Why couldn't I remember these helpful, little unix tools... :-)</p></div><div id="comment-3258-info" class="comment-info"><span class="comment-age">(31 Mar '11, 13:10)</span> <span class="comment-user userinfo">DrJekyll</span></div></div></div><div id="comment-tools-3255" class="comment-tools"></div><div class="clear"></div><div id="comment-3255-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3251"></span>

<div id="answer-container-3251" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3251-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3251-score" class="post-score" title="current number of votes">0</div><span id="post-3251-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe you captured duplicate frames by mirroring more than one switch port or spanning a VLAN. You can try to remove duplicates by running your trace through editcap (installed together with Wireshark) using the -d parameter:</p><pre><code>editcap -d &lt;infile&gt; &lt;outfile&gt;</code></pre><p>The outfile should contain no more duplicates. You may have to adjust editcap's performance using -D or -w, check <code>editcap -h</code>for a list of parameters.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Mar '11, 12:42</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-3251" class="comments-container"><span id="3252"></span><div id="comment-3252" class="comment"><div id="post-3252-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper, thanks for your quick response. I don't have duplicate frames. The SNMP Server repeats his requests with the same request id when he didn't get a reply to a request. I just need the request id which are duplicate.</p></div><div id="comment-3252-info" class="comment-info"><span class="comment-age">(31 Mar '11, 12:51)</span> <span class="comment-user userinfo">DrJekyll</span></div></div><span id="3253"></span><div id="comment-3253" class="comment"><div id="post-3253-score" class="comment-score"></div><div class="comment-text"><p>In that case it may be possible to find those by using the export menu to save the packet list to a CSV file and import that into an excel file or a database. I'd make sure to add a custom column containing the ID (if there is a display filter that reports those, I have no SNMP trace atm) so that it gets exported with the rest. Then you can use makros or database statements to find your duplicate IDs, but don't ask me how to program excel, it's not in my current skillset - maybe just sorting by ID column can help :-)</p></div><div id="comment-3253-info" class="comment-info"><span class="comment-age">(31 Mar '11, 12:54)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="3254"></span><div id="comment-3254" class="comment"><div id="post-3254-score" class="comment-score"></div><div class="comment-text"><p>Probably I will have to do something like this. Can't find a wireshark solution.</p></div><div id="comment-3254-info" class="comment-info"><span class="comment-age">(31 Mar '11, 13:00)</span> <span class="comment-user userinfo">DrJekyll</span></div></div><span id="3256"></span><div id="comment-3256" class="comment"><div id="post-3256-score" class="comment-score"></div><div class="comment-text"><p>I added a column for snmp.request_id field. But the field is always empty. Perhaps there is a bug in wireshark :-(</p></div><div id="comment-3256-info" class="comment-info"><span class="comment-age">(31 Mar '11, 13:04)</span> <span class="comment-user userinfo">DrJekyll</span></div></div><span id="3257"></span><div id="comment-3257" class="comment"><div id="post-3257-score" class="comment-score"></div><div class="comment-text"><p>Which version are you running, it works fine on 1.5.0 SVN 36017 (development version)</p></div><div id="comment-3257-info" class="comment-info"><span class="comment-age">(31 Mar '11, 13:09)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="3259"></span><div id="comment-3259" class="comment not_top_scorer"><div id="post-3259-score" class="comment-score"></div><div class="comment-text"><p>I'm still using 1.4.0. I will update...</p></div><div id="comment-3259-info" class="comment-info"><span class="comment-age">(31 Mar '11, 13:11)</span> <span class="comment-user userinfo">DrJekyll</span></div></div></div><div id="comment-tools-3251" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-3251-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

