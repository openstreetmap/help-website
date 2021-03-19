+++
type = "question"
title = "Couldn&#x27;t extract encrypted Application data from pcap using Perl Netpacket module"
description = '''I tried to extract the encrypted application data using the perl Netpacket module.I am able to see the ports but couldn&#x27;t see the encrypted data.Any Modules are there to see the encrypted app data or any unpack function is required to read that?'''
date = "2013-05-22T23:54:00Z"
lastmod = "2013-05-23T06:20:00Z"
weight = 21392
keywords = [ "decryption", "perl", "pcap", "netpacket" ]
aliases = [ "/questions/21392" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Couldn't extract encrypted Application data from pcap using Perl Netpacket module](/questions/21392/couldnt-extract-encrypted-application-data-from-pcap-using-perl-netpacket-module)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21392-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21392-score" class="post-score" title="current number of votes">0</div><span id="post-21392-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I tried to extract the encrypted application data using the perl Netpacket module.I am able to see the ports but couldn't see the encrypted data.Any Modules are there to see the encrypted app data or any unpack function is required to read that?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-perl" rel="tag" title="see questions tagged &#39;perl&#39;">perl</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-netpacket" rel="tag" title="see questions tagged &#39;netpacket&#39;">netpacket</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 May '13, 23:54</strong></p><img src="https://secure.gravatar.com/avatar/3606fb2f161676306a345c0e2809e550?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kalai&#39;s gravatar image" /><p><span>Kalai</span><br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kalai has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 May '13, 06:25</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-21392" class="comments-container"></div><div id="comment-tools-21392" class="comment-tools"></div><div class="clear"></div><div id="comment-21392-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21394"></span>

<div id="answer-container-21394" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21394-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21394-score" class="post-score" title="current number of votes">1</div><span id="post-21394-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I am able to see the ports but couldn't see the encrypted data.</p></blockquote><p>well, that depends on your code. If you post the code somewhere I'm willing to check it.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 May '13, 01:50</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-21394" class="comments-container"><span id="21396"></span><div id="comment-21396" class="comment"><div id="post-21396-score" class="comment-score"></div><div class="comment-text"><p>0</p><p>The code snippet is,</p><pre><code>sub func( my($pcapfile, $header, $pcapPacket) = @_; # unpack ethernet header
  my $ethObj = NetPacket::Ethernet-&gt;decode($pcapPacket); # unpack ip header
  my $ipObj = NetPacket::IP-&gt;decode($ethObj-&gt;{data}); # unpack udp header
  my $pktObj;

  if ($ipObj-&gt;{proto} == IP_PROTO_TCP) {
    $pktObj = NetPacket::TCP-&gt;decode($ipObj-&gt;{data});
    print $pktObj-&gt;{src_port}
    print $pktObj-&gt;{dest_port}
    print $pktObj-&gt;{data};
  }
)</code></pre><p>Its printing ports properly..but some junk values for data.any unpack function need to use to decode the ssl encrypted app data?</p></div><div id="comment-21396-info" class="comment-info"><span class="comment-age">(23 May '13, 01:55)</span> <span class="comment-user userinfo">Kalai</span></div></div><span id="21398"></span><div id="comment-21398" class="comment"><div id="post-21398-score" class="comment-score"></div><div class="comment-text"><p>code looks O.K. (generally).</p><blockquote><p>but some junk values for data.</p></blockquote><p>that's the <strong>binary</strong> data of the payload.</p><p>What did you expect to get?</p><p>BTW: Just a reminder. You cannot <strong>decrypt</strong> the data with NetPacket.</p></div><div id="comment-21398-info" class="comment-info"><span class="comment-age">(23 May '13, 02:12)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="21399"></span><div id="comment-21399" class="comment"><div id="post-21399-score" class="comment-score"></div><div class="comment-text"><p>Yes it wont decrypt.I just want to see the encrypted application data in hex like wireshark shows.can it be possible?</p></div><div id="comment-21399-info" class="comment-info"><span class="comment-age">(23 May '13, 02:18)</span> <span class="comment-user userinfo">Kalai</span></div></div><span id="21401"></span><div id="comment-21401" class="comment"><div id="post-21401-score" class="comment-score"></div><div class="comment-text"><p>Yes I am able to see when I convert binary data into hex value..Thanks for the input...</p></div><div id="comment-21401-info" class="comment-info"><span class="comment-age">(23 May '13, 02:40)</span> <span class="comment-user userinfo">Kalai</span></div></div><span id="21405"></span><div id="comment-21405" class="comment"><div id="post-21405-score" class="comment-score"></div><div class="comment-text"><blockquote><p>when I convert binary data into hex value</p></blockquote><p>yes, that's the way to do it.</p></div><div id="comment-21405-info" class="comment-info"><span class="comment-age">(23 May '13, 06:20)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-21394" class="comment-tools"></div><div class="clear"></div><div id="comment-21394-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

