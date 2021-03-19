+++
type = "question"
title = "`make -C plugins` fails looking for target tools/lemon/lemon.c"
description = '''I&#x27;m running on Ubuntu 16.04 LTS (xenial). I cloned the source from: https://code.wireshark.org/review/wireshark This is the output of ./configure The Wireshark package has been configured with the following options:  GLib version : v2.48.0  Build wireshark : yes (with Qt4 v4.8.7)  Build wireshark-gt...'''
date = "2016-04-28T05:54:00Z"
lastmod = "2016-04-28T08:21:00Z"
weight = 52045
keywords = [ "make", "plugins" ]
aliases = [ "/questions/52045" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [\`make -C plugins\` fails looking for target tools/lemon/lemon.c](/questions/52045/make-c-plugins-fails-looking-for-target-toolslemonlemonc)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52045-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52045-score" class="post-score" title="current number of votes">0</div><span id="post-52045-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm running on Ubuntu 16.04 LTS (xenial).</p><p>I cloned the source from: <a href="https://code.wireshark.org/review/wireshark">https://code.wireshark.org/review/wireshark</a></p><p>This is the output of <code>./configure</code></p><pre><code>The Wireshark package has been configured with the following options:
                       GLib version : v2.48.0
                    Build wireshark : yes (with Qt4 v4.8.7)
                Build wireshark-gtk : no
                       Build tshark : yes
                      Build tfshark : no
                     Build capinfos : yes
                      Build captype : yes
                      Build editcap : yes
                      Build dumpcap : yes
                     Build mergecap : yes
                   Build reordercap : yes
                    Build text2pcap : yes
                      Build randpkt : yes
                       Build dftest : yes
                     Build rawshark : yes
                  Build androiddump : yes
                      Build sshdump : no
                    Build ciscodump : no
                  Build randpktdump : yes
                        Build echld : no

   Save files as pcap-ng by default : yes
  Install dumpcap with capabilities : no
             Install dumpcap setuid : no
                  Use dumpcap group : (none)
                        Use plugins : yes
       Use external capture sources : yes
                    Use Lua library : no
                Build Qt RTP player : no
              Build GTK+ RTP player : no
             Build profile binaries : no
                   Use pcap library : yes
                   Use zlib library : yes
               Use kerberos library : no
                 Use c-ares library : no (name resolution will be disabled)
                Use SMI MIB library : no
             Use GNU gcrypt library : yes
             Use SSL crypto library : no
                 Use GnuTLS library : no
     Use POSIX capabilities library : yes
                  Use GeoIP library : no
                 Use libssh library : no
            Have ssh_userauth_agent : no
                     Use nl library : no
              Use SBC codec library : no</code></pre><p>This is the output of <code>$make -C plugins</code>:</p><pre><code>make: Entering directory &#39;/root/wireshark/plugins&#39;
...
Making all in mate
make[1]: Entering directory &#39;/root/wireshark/plugins/mate&#39;
gcc -g -O2    ../../tools/lemon/lemon.c   -o ../../tools/lemon/lemon
../../tools/lemon/lemon.c:10:20: fatal error: config.h: No such file or directory
compilation terminated.
&lt;builtin&gt;: recipe for target &#39;../../tools/lemon/lemon&#39; failed
make[1]: *** [../../tools/lemon/lemon] Error 1
make[1]: Leaving directory &#39;/root/wireshark/plugins/mate&#39;
Makefile:564: recipe for target &#39;all-recursive&#39; failed
make: *** [all-recursive] Error 1
make: Leaving directory &#39;/root/wireshark/plugins&#39;</code></pre><p>Any ideas on what's wrong and how to fix?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-make" rel="tag" title="see questions tagged &#39;make&#39;">make</span> <span class="post-tag tag-link-plugins" rel="tag" title="see questions tagged &#39;plugins&#39;">plugins</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Apr '16, 05:54</strong></p><img src="https://secure.gravatar.com/avatar/693e366f746758be7fcd22b135bc0e07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="embr&#39;s gravatar image" /><p><span>embr</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="embr has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Apr '16, 05:57</strong> </span></p></div></div><div id="comments-container-52045" class="comments-container"></div><div id="comment-tools-52045" class="comment-tools"></div><div class="clear"></div><div id="comment-52045-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="52050"></span>

<div id="answer-container-52050" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52050-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52050-score" class="post-score" title="current number of votes">1</div><span id="post-52050-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="embr has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It seems you need to make lemon first:</p><pre><code>make -C tools/lemon</code></pre><p>I'll submit a change so that's not necessary.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '16, 07:48</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-52050" class="comments-container"><span id="52051"></span><div id="comment-52051" class="comment"><div id="post-52051-score" class="comment-score"></div><div class="comment-text"><p>Change is: <a href="https://code.wireshark.org/review/15143">https://code.wireshark.org/review/15143</a></p></div><div id="comment-52051-info" class="comment-info"><span class="comment-age">(28 Apr '16, 07:52)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="52052"></span><div id="comment-52052" class="comment"><div id="post-52052-score" class="comment-score"></div><div class="comment-text"><p>I am currently in the process of compiling wireshark (which, I figure, includes tools/lemon). Once it finishes I'll clean it and try again by making lemon alone.</p></div><div id="comment-52052-info" class="comment-info"><span class="comment-age">(28 Apr '16, 07:52)</span> <span class="comment-user userinfo">embr</span></div></div><span id="52054"></span><div id="comment-52054" class="comment"><div id="post-52054-score" class="comment-score"></div><div class="comment-text"><p>Ok, I'm still having trouble compiling my custom plugin, but I'm now a step closer. Thanks for the help.</p></div><div id="comment-52054-info" class="comment-info"><span class="comment-age">(28 Apr '16, 08:21)</span> <span class="comment-user userinfo">embr</span></div></div></div><div id="comment-tools-52050" class="comment-tools"></div><div class="clear"></div><div id="comment-52050-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="52048"></span>

<div id="answer-container-52048" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52048-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52048-score" class="post-score" title="current number of votes">1</div><span id="post-52048-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><ol><li>You should not build this (or any) package as root</li><li>build wireshark proper, before going into building plugins</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '16, 07:24</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-52048" class="comments-container"><span id="52049"></span><div id="comment-52049" class="comment"><div id="post-52049-score" class="comment-score"></div><div class="comment-text"><ol><li>Can you explain why? I am working on a VM built for the sole purpose of experimenting with wireshark plugins. If there is a technical reason why building packages as root is going to mess up the process I'd like to hear it.</li></ol></div><div id="comment-52049-info" class="comment-info"><span class="comment-age">(28 Apr '16, 07:42)</span> <span class="comment-user userinfo">embr</span></div></div><span id="52053"></span><div id="comment-52053" class="comment"><div id="post-52053-score" class="comment-score"></div><div class="comment-text"><p>It's not going to mess up the process it's just a Really Bad Idea.</p><p>It's just a general rule: don't do anything as root unless it can't be done as a normal (non-root) user.</p></div><div id="comment-52053-info" class="comment-info"><span class="comment-age">(28 Apr '16, 07:53)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-52048" class="comment-tools"></div><div class="clear"></div><div id="comment-52048-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

