+++
type = "question"
title = "Can&#x27;t export mac address as CSV"
description = '''I am trying to use Tshark to analyze network traffic to find probe requests on a wifi card in monitor mode. I would like to use tshark to analyze traffic than output the data into a csv file. I can capture the data in real time with:  tshark -i wlan1 -f &quot;type mgt subtype probe-req&quot;  but if i try and...'''
date = "2017-07-11T10:32:00Z"
lastmod = "2017-07-12T07:04:00Z"
weight = 62675
keywords = [ "-tfields", "filter", "tshark" ]
aliases = [ "/questions/62675" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can't export mac address as CSV](/questions/62675/cant-export-mac-address-as-csv)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62675-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62675-score" class="post-score" title="current number of votes">0</div><span id="post-62675-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to use Tshark to analyze network traffic to find probe requests on a wifi card in monitor mode. I would like to use tshark to analyze traffic than output the data into a csv file. I can capture the data in real time with:</p><pre><code>tshark -i wlan1 -f &quot;type mgt subtype probe-req&quot;</code></pre><p>but if i try and use:</p><pre><code>-i wlan1 -f &quot;type mgt subtype probe-req&quot; -T fields -e frame.number -e wlan.sa ...(every mac/ip filter i could find) -E separator=,</code></pre><p>all i get is the frame number. Am i using the -T field/-e fields commands wrong or am i missing something?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link--tfields" rel="tag" title="see questions tagged &#39;-tfields&#39;">-tfields</span> <span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jul '17, 10:32</strong></p><img src="https://secure.gravatar.com/avatar/2f31b75290dfe8b68a3e354281d32a2c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="20weegweeg&#39;s gravatar image" /><p><span>20weegweeg</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="20weegweeg has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Jul '17, 10:54</strong> </span></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-62675" class="comments-container"><span id="62676"></span><div id="comment-62676" class="comment"><div id="post-62676-score" class="comment-score"></div><div class="comment-text"><p>Do you experience the same issue if you use</p><pre><code>tshark -i wlan1 -f &quot;type mgt subtype probe-req&quot; -w my_file

tshark -r my_file -T fields -e frame.number -e wlan.sa -E separator=,</code></pre><p>?</p></div><div id="comment-62676-info" class="comment-info"><span class="comment-age">(11 Jul '17, 10:58)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-62675" class="comment-tools"></div><div class="clear"></div><div id="comment-62675-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62686"></span>

<div id="answer-container-62686" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62686-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62686-score" class="post-score" title="current number of votes">0</div><span id="post-62686-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What version of Wireshark is this?</p><pre><code>./tshark -i en0 -I -T fields -e frame.number -e wlan.sa -f &quot;type mgt subtype probe-req&quot; -E separator=,</code></pre><p>printed</p><pre><code>1,{MAC address 1}
2,{MAC address 1}
3,{MAC address 1}
4,{MAC address 2}
5,{MAC address 2}</code></pre><p>on my MacBook Pro with a build from a recent checkout of the master branch.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jul '17, 18:54</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-62686" class="comments-container"><span id="62704"></span><div id="comment-62704" class="comment"><div id="post-62704-score" class="comment-score"></div><div class="comment-text"><p>I installed the latest build and now it works, thanks for the help</p></div><div id="comment-62704-info" class="comment-info"><span class="comment-age">(12 Jul '17, 07:04)</span> <span class="comment-user userinfo">20weegweeg</span></div></div></div><div id="comment-tools-62686" class="comment-tools"></div><div class="clear"></div><div id="comment-62686-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

