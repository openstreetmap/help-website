+++
type = "question"
title = "how to set capture filter for different MPLS label"
description = '''Guys,  I am trying to use TShark to capture ip packets with 172.16.1.1/2 or 172.16.2.1/2 and mpls packets with 2 layer label (23,25) or 1 layer label 19 at the same time with below command but failed tshark -i eth1 -w test2.cap &#x27;(net 172.16.2.0/30 or 172.16.1.0/30) or (mpls and mpls 19) or (mpls 23 ...'''
date = "2010-12-13T19:08:00Z"
lastmod = "2010-12-14T05:57:00Z"
weight = 1334
keywords = [ "different", "labels", "mpls" ]
aliases = [ "/questions/1334" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to set capture filter for different MPLS label](/questions/1334/how-to-set-capture-filter-for-different-mpls-label)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1334-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1334-score" class="post-score" title="current number of votes">2</div><span id="post-1334-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Guys, I am trying to use TShark to capture ip packets with 172.16.1.1/2 or 172.16.2.1/2 and mpls packets with 2 layer label (23,25) or 1 layer label 19 at the same time with below command but failed</p><p>tshark -i eth1 -w test2.cap '(net 172.16.2.0/30 or 172.16.1.0/30) or (mpls and mpls 19) or (mpls 23 and mpls 25)'</p><p>it seems like only the first "mpls and mpls 19" filter will work....do any of you guys can tell if we can capture 2 layer label (23,25) and 1 layer label 19 at the same time please?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-different" rel="tag" title="see questions tagged &#39;different&#39;">different</span> <span class="post-tag tag-link-labels" rel="tag" title="see questions tagged &#39;labels&#39;">labels</span> <span class="post-tag tag-link-mpls" rel="tag" title="see questions tagged &#39;mpls&#39;">mpls</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Dec '10, 19:08</strong></p><img src="https://secure.gravatar.com/avatar/9df416451ecae22ccd97710f7413abc8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alexzhao&#39;s gravatar image" /><p><span>alexzhao</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alexzhao has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Dec '10, 19:09</strong> </span></p></div></div><div id="comments-container-1334" class="comments-container"></div><div id="comment-tools-1334" class="comment-tools"></div><div class="clear"></div><div id="comment-1334-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1336"></span>

<div id="answer-container-1336" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1336-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1336-score" class="post-score" title="current number of votes">1</div><span id="post-1336-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>First of all, capture filters use BPF filters and BPF is based on a tiny state machine with a few machine instructions. You can show the code that will be used by a capture filter by using dumpcap -d or tcpdump -d.</p><p>Whenever a keyword is used in a capture filter that denotes an encapsulation (vlan, mpls, ppp, etc), the offset into the packet is increased by the size of the encapsulation header. So in your case, each mpls keyword increases the offset with 4 bytes. This results in BPF code that looks at the wrong place for your mpls labels. As can be seen in the following output (restricted to the first part of your filter):</p><pre><code>$ tcpdump -d &#39;(mpls and mpls 19)&#39;
(000) ldh      [12]
(001) jeq      #0x8847          jt 2    jf 8
(002) ldb      [16]
(003) jset     #0x1             jt 8    jf 4
(004) ld       [18]
(005) and      #0xfffff000
(006) jeq      #0x13000         jt 7    jf 8
(007) ret      #65535
(008) ret      #0
$</code></pre><p>The first mpls label starts at offset 14 and the second at offset 18. However, the generated code first looks at the "bottom of stack" bit of the first mpls header and then checks the actual label in the second mpls header. So using mpls keywords multiple times in a filter will not help you.</p><p>The only way to get the result you want is to manually look at the proper locations for your mpls labels. You can change your filter (only the mpls part) to:</p><pre><code>$ tcpdump -d &#39;mpls and ( 
    (ether[14:4]&amp;0xfffff100=0x13100) or 
    (ether[14:4]&amp;0xfffff100=0x17000 and ether[18:4]&amp;0xfffff100=0x19100) 
  )&#39;
(000) ldh      [12]
(001) jeq      #0x8847          jt 2    jf 10
(002) ld       [14]
(003) and      #0xfffff100
(004) jeq      #0x13100         jt 9    jf 5
(005) jeq      #0x17000         jt 6    jf 10
(006) ld       [18]
(007) and      #0xfffff100
(008) jeq      #0x19100         jt 9    jf 10
(009) ret      #65535
(010) ret      #0
$</code></pre><p>(I have split the command for readability, it should be on one line though)</p><p>This filter first checks for the mpls ethertype. Then it checks the first mpls header to see whether label 19 is present and that it is the last label in the stack. If not, it checks whether label 23 is present and that label 23 is not the last label. In case of the latter, it then checks the second mpls header to see whether it has label 25 and that is now is the last label in the stack.</p><p>I don't have a MPLS trace with multiple labels to experiment with, but looking at the generated BPF code, I think it should work :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '10, 01:02</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-1336" class="comments-container"><span id="1341"></span><div id="comment-1341" class="comment"><div id="post-1341-score" class="comment-score"></div><div class="comment-text"><p>Thanks, it perfectly resolved my question and give me a new way to capture packets with T-shark filter.</p></div><div id="comment-1341-info" class="comment-info"><span class="comment-age">(14 Dec '10, 05:32)</span> <span class="comment-user userinfo">alexzhao</span></div></div><span id="1343"></span><div id="comment-1343" class="comment"><div id="post-1343-score" class="comment-score"></div><div class="comment-text"><p>I converted your answer to a comment, please have a look at :</p><p>http://ask.wireshark.org/questions/292/example-of-how-to-use-askwiresharkorg-and-how-not-to</p><p>to know why :-)</p></div><div id="comment-1343-info" class="comment-info"><span class="comment-age">(14 Dec '10, 05:57)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-1336" class="comment-tools"></div><div class="clear"></div><div id="comment-1336-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

