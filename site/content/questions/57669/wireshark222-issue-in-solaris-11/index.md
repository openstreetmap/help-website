+++
type = "question"
title = "Wireshark2.2.2 issue in solaris 11"
description = '''Hi, I am not able to compile wirehshark on Solaris 11, there is no issues while ./configure but its failing in make with below errors. version.h unchanged.  CC wireshark_gtk-ws_version_info.o  CCLD wireshark-gtk libtool: link: not configured to extract global symbols from dlpreopened files ld: warni...'''
date = "2016-11-27T21:00:00Z"
lastmod = "2016-12-02T13:21:00Z"
weight = 57669
keywords = [ "libwireshark", "solaris", "build" ]
aliases = [ "/questions/57669" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark2.2.2 issue in solaris 11](/questions/57669/wireshark222-issue-in-solaris-11)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57669-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57669-score" class="post-score" title="current number of votes">0</div><span id="post-57669-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am not able to compile wirehshark on Solaris 11, there is no issues while ./configure but its failing in make with below errors.</p><pre><code>version.h unchanged.
  CC     wireshark_gtk-ws_version_info.o
  CCLD   wireshark-gtk
libtool: link: not configured to extract global symbols from dlpreopened files
ld: warning: file /root/WIRESHARK/2.2.2/wireshark-2.2.2/wiretap/.libs/libwiretap.so: linked to wiretap/.libs/libwiretap.so: attempted multiple inclusion of file
ld: warning: file wsutil/.libs/libwsutil.so: linked to /root/WIRESHARK/2.2.2/wireshark-2.2.2/wsutil/.libs/libwsutil.so: attempted multiple inclusion of file
ld: warning: global symbol &#39;END&#39; has non-global binding:
        (file /usr/local/lib/libpcap.so value=LOCL);
ld: warning: global symbol &#39;START&#39; has non-global binding:
        (file /usr/local/lib/libpcap.so value=LOCL);
Undefined                       first referenced
 symbol                             in file
.LC1555                             epan/.libs/libwireshark.so
ld: fatal: symbol referencing errors
collect2: ld returned 1 exit status
make[2]:  [wireshark-gtk] Error 1
make[2]: Leaving directory /root/WIRESHARK/2.2.2/wireshark-2.2.2&#39;
make[1]: *** [all-recursive] Error 1
make[1]: Leaving directory/root/WIRESHARK/2.2.2/wireshark-2.2.2&#39;
make:  [all] Error 2
You have new mail in /var/mail/root
[email protected]:~/WIRESHARK/2.2.2/wireshark-2.2.2# </code></pre>Can anyone please help me to relsove this issue. what is the meaning of that symbol in error log.<p>Thanks, Bibin</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-libwireshark" rel="tag" title="see questions tagged &#39;libwireshark&#39;">libwireshark</span> <span class="post-tag tag-link-solaris" rel="tag" title="see questions tagged &#39;solaris&#39;">solaris</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Nov '16, 21:00</strong></p><img src="https://secure.gravatar.com/avatar/8a1bb66d475e6ceec4ae17d184deecc5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bibin&#39;s gravatar image" /><p><span>Bibin</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bibin has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Nov '16, 21:58</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-57669" class="comments-container"></div><div id="comment-tools-57669" class="comment-tools"></div><div class="clear"></div><div id="comment-57669-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57677"></span>

<div id="answer-container-57677" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57677-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57677-score" class="post-score" title="current number of votes">0</div><span id="post-57677-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><a href="https://lists.gnu.org/archive/html/libtool/2012-11/msg00006.html">This thread</a> suggests that the problem is that <code>configure</code> found an <code>nm</code> that doesn't provide BSD-style output. (It also provides a fix/workaround if that's the case.)</p><p>There are a number of other threads to be found on the 'net which discuss that error message but most others appear to be dealing with cross-compiling (you're not trying to do that, are you?).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Nov '16, 06:07</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-57677" class="comments-container"><span id="57687"></span><div id="comment-57687" class="comment"><div id="post-57687-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the response..</p><p>No am not using any other thread.</p><p>Can you please provide a detail workaround to overcome this issue ?</p><p>Thanks, Bibin</p></div><div id="comment-57687-info" class="comment-info"><span class="comment-age">(28 Nov '16, 22:09)</span> <span class="comment-user userinfo">Bibin</span></div></div><span id="57697"></span><div id="comment-57697" class="comment"><div id="post-57697-score" class="comment-score"></div><div class="comment-text"><p>Could it be related to linker flags being different on Solaris and GCC? <a href="https://sourceforge.net/p/polybori/bugs/9/">https://sourceforge.net/p/polybori/bugs/9/</a></p></div><div id="comment-57697-info" class="comment-info"><span class="comment-age">(29 Nov '16, 04:24)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="57767"></span><div id="comment-57767" class="comment"><div id="post-57767-score" class="comment-score"></div><div class="comment-text"><p>Sorry, I'm not sure what you mean by not using any other thread. Do you mean you're not cross compiling?</p><p>Did you try the NM workaround mentioned in the link?</p></div><div id="comment-57767-info" class="comment-info"><span class="comment-age">(01 Dec '16, 11:35)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="57801"></span><div id="comment-57801" class="comment"><div id="post-57801-score" class="comment-score"></div><div class="comment-text"><blockquote><p><code>file /usr/local/lib/libpcap.so</code></p></blockquote><p>What version of libpcap is that? Did you build it from source?</p></div><div id="comment-57801-info" class="comment-info"><span class="comment-age">(02 Dec '16, 13:21)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-57677" class="comment-tools"></div><div class="clear"></div><div id="comment-57677-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

