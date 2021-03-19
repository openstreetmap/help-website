+++
type = "question"
title = "Building tshark with ssl?"
description = '''I&#x27;m trying to build tshark and dig into its ssl decoding, but it doesn&#x27;t seem to want to include the ssl decoder and I&#x27;m not sure why; I looked around briefly to see if the dissectors get dynamically loaded somehow, but don&#x27;t see that either: # configure --disable-wireshark --with-ssl --without-gnut...'''
date = "2015-11-05T12:20:00Z"
lastmod = "2015-11-06T05:21:00Z"
weight = 47312
keywords = [ "ssl", "tshark" ]
aliases = [ "/questions/47312" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Building tshark with ssl?](/questions/47312/building-tshark-with-ssl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47312-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47312-score" class="post-score" title="current number of votes">0</div><span id="post-47312-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to build tshark and dig into its ssl decoding, but it doesn't seem to want to include the ssl decoder and I'm not sure why; I looked around briefly to see if the dissectors get dynamically loaded somehow, but don't see that either:</p><pre><code># configure --disable-wireshark --with-ssl --without-gnutls
...
The Wireshark package has been configured with the following options.
                    Build wireshark : no
                       Build tshark : yes
                     Build capinfos : yes
                      Build editcap : yes
                      Build dumpcap : yes
                     Build mergecap : yes
                    Build text2pcap : yes
                      Build randpkt : yes
                       Build dftest : yes
                     Build rawshark : yes

   Save files as pcap-ng by default : yes
  Install dumpcap with capabilities : no
             Install dumpcap setuid : no
                  Use dumpcap group : (none)
                        Use plugins : yes
                    Use Lua library : no
                 Use Python binding : no
                   Build rtp_player : no
             Build profile binaries : no
                   Use pcap library : yes
                   Use zlib library : yes
               Use kerberos library : yes (MIT)
                 Use c-ares library : no
               Use GNU ADNS library : no
                Use SMI MIB library : no
             Use GNU crypto library : no
             Use SSL crypto library : yes
           Use IPv6 name resolution : yes
                 Use gnutls library : no
     Use POSIX capabilities library : no
                  Use GeoIP library : no

# make
...
# strings .libs/tshark | grep ssl
#</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Nov '15, 12:20</strong></p><img src="https://secure.gravatar.com/avatar/e4593780df11bb64273008c2f8925227?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="abatie&#39;s gravatar image" /><p><span>abatie</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="abatie has no accepted answers">0%</span></p></div></div><div id="comments-container-47312" class="comments-container"></div><div id="comment-tools-47312" class="comment-tools"></div><div class="clear"></div><div id="comment-47312-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="47314"></span>

<div id="answer-container-47314" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47314-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47314-score" class="post-score" title="current number of votes">1</div><span id="post-47314-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>tshark is loading libwireshark library that contains all dissectors code, including SSL:</p><p>strings epan/.libs/libwireshark.so</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Nov '15, 13:01</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-47314" class="comments-container"></div><div id="comment-tools-47314" class="comment-tools"></div><div class="clear"></div><div id="comment-47314-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="47315"></span>

<div id="answer-container-47315" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47315-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47315-score" class="post-score" title="current number of votes">0</div><span id="post-47315-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Based on your configure output it seems that you are building an old version of Wireshark.</p><pre><code>                 Build mergecap : yes
             [reordercap is missing here]
                Build text2pcap : yes</code></pre><p>You are probably using versions older than 1.6.11, 1.8.9 or 1.10.0. You are suggested to use at least 1.12.x now (or 2.0 which is around the corner). Dissection of SSL/TLS is well supported in Wireshark, though some newer TLS details may require a more recent version of Wireshark.</p><p>If you are instead looking at SSL/TLS <em>decryption</em> rather than dissection, do note that versions before 2.0 require both GnuTLS and Libgcrypt to be enabled for decryption support. Since 2.0, Libgcrypt is sufficient for decryption using a SSL key logfile. GnuTLS is required for RSA keyfiles support though.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Nov '15, 14:06</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-47315" class="comments-container"><span id="47317"></span><div id="comment-47317" class="comment"><div id="post-47317-score" class="comment-score"></div><div class="comment-text"><p>I did both 1.8.10 (to match the package that comes with centos) and 1.12.8. These are both good information as indeed, I am trying to improve the diagnostics when decryption fails. Thanks!</p></div><div id="comment-47317-info" class="comment-info"><span class="comment-age">(05 Nov '15, 14:51)</span> <span class="comment-user userinfo">abatie</span></div></div><span id="47337"></span><div id="comment-47337" class="comment"><div id="post-47337-score" class="comment-score"></div><div class="comment-text"><p><span>@abatie</span> I recommend you to try 1.12 or newer, it already fixed various decryption issues.</p></div><div id="comment-47337-info" class="comment-info"><span class="comment-age">(06 Nov '15, 05:21)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div></div><div id="comment-tools-47315" class="comment-tools"></div><div class="clear"></div><div id="comment-47315-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

