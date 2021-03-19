+++
type = "question"
title = "Anyone knows how to convert .pcap file to plain text file in Java ?"
description = '''I want to convert pcap files in plain text files like Wireshark does, from Java source code. Anyone knows how can I do it?'''
date = "2015-07-28T13:25:00Z"
lastmod = "2015-10-21T13:22:00Z"
weight = 44578
keywords = [ "java", "pcap", "plain-text" ]
aliases = [ "/questions/44578" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Anyone knows how to convert .pcap file to plain text file in Java ?](/questions/44578/anyone-knows-how-to-convert-pcap-file-to-plain-text-file-in-java)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44578-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44578-score" class="post-score" title="current number of votes">0</div><span id="post-44578-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to convert pcap files in plain text files like Wireshark does, from Java source code. Anyone knows how can I do it?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-plain-text" rel="tag" title="see questions tagged &#39;plain-text&#39;">plain-text</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jul '15, 13:25</strong></p><img src="https://secure.gravatar.com/avatar/3ff5f5b5b44acf16d015bcb42f0506cd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Miguel%20Freitas&#39;s gravatar image" /><p><span>Miguel Freitas</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Miguel Freitas has no accepted answers">0%</span></p></div></div><div id="comments-container-44578" class="comments-container"></div><div id="comment-tools-44578" class="comment-tools"></div><div class="clear"></div><div id="comment-44578-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="46810"></span>

<div id="answer-container-46810" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46810-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46810-score" class="post-score" title="current number of votes">1</div><span id="post-46810-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Miguel Freitas has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There are at least two libraries: <a href="https://github.com/kaitoy/pcap4j">pcap4j</a> and <a href="http://jnetpcap.com/">jNetPcap</a>.</p><p>It <a href="http://stackoverflow.com/a/28131027/1587329">seems</a> as though pcap4j is working on OS X, while the other is not. (And it is newer).</p><p>There is a <a href="https://github.com/kaitoy/pcap4j/blob/master/pcap4j-sample/src/main/java/org/pcap4j/sample/ReadPacketFile.java">sample</a> for reading a file:</p><pre><code>package org.pcap4j.sample;

import java.io.EOFException;
import java.util.concurrent.TimeoutException;
import org.pcap4j.core.NotOpenException;
import org.pcap4j.core.PcapHandle;
import org.pcap4j.core.PcapHandle.TimestampPrecision;
import org.pcap4j.core.PcapNativeException;
import org.pcap4j.core.Pcaps;
import org.pcap4j.packet.Packet;

@SuppressWarnings(&quot;javadoc&quot;)
public class ReadPacketFile {

  private static final int COUNT = 5;

  private static final String PCAP_FILE_KEY
    = ReadPacketFile.class.getName() + &quot;.pcapFile&quot;;
  private static final String PCAP_FILE
    = System.getProperty(PCAP_FILE_KEY, &quot;src/main/resources/echoAndEchoReply.pcap&quot;);

  public static void main(String[] args) throws PcapNativeException, NotOpenException {
    PcapHandle handle;
    try {
      handle = Pcaps.openOffline(PCAP_FILE, TimestampPrecision.NANO);
    } catch (PcapNativeException e) {
      handle = Pcaps.openOffline(PCAP_FILE);
    }

    for (int i = 0; i &lt; COUNT; i++) {
      try {
        Packet packet = handle.getNextPacketEx();
        System.out.println(handle.getTimestamp());
        System.out.println(packet);
      } catch (TimeoutException e) {
      } catch (EOFException e) {
        System.out.println(&quot;EOF&quot;);
        break;
      }
    }

    handle.close();
  }
}</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '15, 10:49</strong></p><img src="https://secure.gravatar.com/avatar/0f479a594deab60e820a84e87409f955?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="user1234&#39;s gravatar image" /><p><span>user1234</span><br />
<span class="score" title="56 reputation points">56</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="user1234 has one accepted answer">50%</span></p></div></div><div id="comments-container-46810" class="comments-container"></div><div id="comment-tools-46810" class="comment-tools"></div><div class="clear"></div><div id="comment-46810-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46818"></span>

<div id="answer-container-46818" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46818-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46818-score" class="post-score" title="current number of votes">0</div><span id="post-46818-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>While there are some pcap libraries for Java (as mentioned by <span>@user1234</span>), they don't have (by far) the dissection functionality of Wireshark. As there is no (official) Wireshark library to use, you can run tshark (CLI tool) and parse the output with Java.</p><p>See the following similar questions:</p><blockquote><p><a href="https://ask.wireshark.org/questions/38939/pipe-tshark-output-to-java-program">https://ask.wireshark.org/questions/38939/pipe-tshark-output-to-java-program</a><br />
<a href="https://ask.wireshark.org/questions/11153/does-wireshark-have-an-api">https://ask.wireshark.org/questions/11153/does-wireshark-have-an-api</a><br />
<a href="https://ask.wireshark.org/questions/29902/running-wireshark-continuously">https://ask.wireshark.org/questions/29902/running-wireshark-continuously</a><br />
</p></blockquote><p>In my answer to the following question I mentioned some links to the 'unofficial' libwireshark. Maybe you can adapt some of the methods for your Java tool.</p><blockquote><p><a href="https://ask.wireshark.org/questions/33630/library-for-display-filters">https://ask.wireshark.org/questions/33630/library-for-display-filters</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '15, 13:22</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-46818" class="comments-container"></div><div id="comment-tools-46818" class="comment-tools"></div><div class="clear"></div><div id="comment-46818-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

