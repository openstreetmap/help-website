+++
type = "question"
title = "Can&#x27;t filter MAC address in a CAP file, help?"
description = '''Hey guys, I have 80 gigs of capture logs in CAP files. I need to filter a specific MAC address from those in order to save the files to a much smaller file size. For some reason, I am able to find the MAC address by looking at the Source address from within 1 of the CAP files but if I try to filter ...'''
date = "2012-12-22T15:02:00Z"
lastmod = "2012-12-22T15:29:00Z"
weight = 17180
keywords = [ "filter", "mac", "cap", "address" ]
aliases = [ "/questions/17180" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can't filter MAC address in a CAP file, help?](/questions/17180/cant-filter-mac-address-in-a-cap-file-help)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17180-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17180-score" class="post-score" title="current number of votes">0</div><span id="post-17180-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey guys, I have 80 gigs of capture logs in CAP files. I need to filter a specific MAC address from those in order to save the files to a much smaller file size. For some reason, I am able to find the MAC address by looking at the Source address from within 1 of the CAP files but if I try to filter that MAC address from the file it finds nothing. My filter is: eth.addr==xx:xx:xx:xx:xx:xx</p><p>What am I doing wrong? Thanks a lot !</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-cap" rel="tag" title="see questions tagged &#39;cap&#39;">cap</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Dec '12, 15:02</strong></p><img src="https://secure.gravatar.com/avatar/b8c003f9ec879d7c36eb684211da0973?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gaarzen&#39;s gravatar image" /><p><span>Gaarzen</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gaarzen has no accepted answers">0%</span></p></div></div><div id="comments-container-17180" class="comments-container"></div><div id="comment-tools-17180" class="comment-tools"></div><div class="clear"></div><div id="comment-17180-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17182"></span>

<div id="answer-container-17182" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17182-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17182-score" class="post-score" title="current number of votes">0</div><span id="post-17182-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It looks like you are doing it right. What happens if you select the source address and then rightclick on it and chose for "prepare as filter". What does it show in the filter field now?</p><p>When I have to extract data from a collection of pcap files I do it in a command shell and I try to use tcpdump instead of tshark if my filter can be done with BPF filters. This works much quicker as there is no need to do full dissection of the packets. Here's my recipe :-)</p><pre><code>mkdir tmp
for file in *.pcap
do
   tcpdump -r $file -w tmp/$file &quot;ether host xx:xx:xx:xx:xx:xx&quot;
done
mergecap -w extract.pcap tmp/*
rm -rf tmp</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Dec '12, 15:29</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-17182" class="comments-container"></div><div id="comment-tools-17182" class="comment-tools"></div><div class="clear"></div><div id="comment-17182-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

